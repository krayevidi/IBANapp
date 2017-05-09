from functools import partial

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from bank_accounts.models import Account
from bank_accounts.tests.factories import AccountFactory
from core.tests.factories import UserFactory


class TestAccountAPIViewsAuthorizedUser(APITestCase):
    def setUp(self):
        self.urls = {
            'account_list': reverse('bank-accounts-api:account-list'),
            'account_detail': partial(reverse,
                                      'bank-accounts-api:account-detail')
        }
        self.user = UserFactory()
        self.client.force_authenticate(self.user)
        self.account_required_fields = {
            'read': [
                'id',
                'first_name',
                'last_name',
                'iban'
            ],
            'write': [
                'first_name',
                'last_name',
                'iban'
            ]
        }
        invalid_string = 'a' * 256
        self.account_data = {
            'valid': {
                'first_name': 'Tony',
                'last_name': 'Stark',
                'iban': 'DE89370400440532013000'
            },
            'invalid': {
                'first_name': invalid_string,
                'last_name': invalid_string,
                'iban': 'invalid'
            }
        }

    def test_account_list_api_view(self):
        """
        Ensure API view will return list of accounts (contains required fields)
        that belongs to authenticated user.
        """
        another_user = UserFactory()
        another_account_list = AccountFactory.create_batch(
            5, manager=another_user
        )
        user_account_list = AccountFactory.create_batch(5, manager=self.user)
        user_account_id_list = [a.id for a in user_account_list]

        response = self.client.get(self.urls['account_list'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_account_id_list = []

        for account in response.data:
            self.assertListEqual(account.keys(),
                                 self.account_required_fields['read'])
            response_account_id_list.append(account['id'])
        self.assertListEqual(user_account_id_list, response_account_id_list)

    def test_create_account_with_empty_data(self):
        """
        Ensure API view will return appropriate errors if empty data
        has been sent.
        """
        data = {}
        response = self.client.post(self.urls['account_list'], data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(self.account_required_fields['write'],
                             response.data.keys())
        self.assertFalse(Account.objects.exists())

    def test_create_account_with_invalid_data(self):
        """
        Ensure API view will return appropriate errors if invalid data
        has been sent.
        """
        data = self.account_data['invalid']
        response = self.client.post(self.urls['account_list'], data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(data.keys(), response.data.keys())
        self.assertFalse(Account.objects.exists())

    def test_create_account_with_valid_data(self):
        """
        Ensure correct account will be created in DB.
        """
        data = self.account_data['valid']
        response = self.client.post(self.urls['account_list'], data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_account = Account.objects.get(iban=data['iban'])
        for field_name, value in data.items():
            self.assertEqual(getattr(created_account, field_name), value)
        self.assertEqual(created_account.manager, self.user)

    def test_account_detail_api_view_owner(self):
        """
        Ensure API view will return account (contains required fields)
        that belongs to authenticated user.
        """
        account = AccountFactory(manager=self.user)
        url = self.urls['account_detail'](kwargs={'pk': account.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(response.data.keys(),
                             self.account_required_fields['read'])

    def test_account_detail_api_view_not_owner(self):
        """
        Ensure API view will return 404 status code to request with any of
        GET, PUT, DELETE methods if requested account does not
        belongs to authenticated user.
        """
        another_user = UserFactory()
        account = AccountFactory(manager=another_user)
        url = self.urls['account_detail'](kwargs={'pk': account.pk})
        response_list = [
            self.client.get(url),
            self.client.put(url),
            self.client.delete(url),
        ]
        for response in response_list:
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_account_with_empty_data(self):
        """
        Ensure account will not be modified in DB and API view will return
        appropriate errors if empty data has been sent.
        """
        account = AccountFactory(manager=self.user)
        required_fields = self.account_required_fields['write']
        data = {}
        url = self.urls['account_detail'](kwargs={'pk': account.pk})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(required_fields, response.data.keys())
        account_from_db = Account.objects.get(pk=account.pk)
        for field in required_fields:
            self.assertEqual(getattr(account, field),
                             getattr(account_from_db, field))

    def test_update_account_with_invalid_data(self):
        """
        Ensure account will not be modified in DB and API view will return
        appropriate errors if invalid data has been sent.
        """
        account = AccountFactory(manager=self.user)
        data = self.account_data['invalid']
        url = self.urls['account_detail'](kwargs={'pk': account.pk})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(data.keys(), response.data.keys())
        account_from_db = Account.objects.get(pk=account.pk)
        for field_name in data.keys():
            self.assertEqual(getattr(account, field_name),
                             getattr(account_from_db, field_name))

    def test_update_account_with_valid_data(self):
        """
        Ensure account will be correctly modified in DB.
        """
        data = self.account_data['valid']
        account = AccountFactory(manager=self.user)
        url = self.urls['account_detail'](kwargs={'pk': account.pk})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        account_from_db = Account.objects.get(pk=account.pk)
        for field_name, value in data.items():
            self.assertEqual(getattr(account_from_db, field_name), value)

    def test_delete_account(self):
        """
        Ensure account will be deleted from DB.
        """
        account = AccountFactory(manager=self.user)
        url = self.urls['account_detail'](kwargs={'pk': account.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Account.DoesNotExist) as _:
            Account.objects.get(pk=account.pk)
