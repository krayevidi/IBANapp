from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from bank_accounts.models import Account
from bank_accounts.tests.factories import AccountFactory
from core.tests.factories import UserFactory


class TestAccountAPIViewsAuthorizedUser(APITestCase):
    def setUp(self):
        self.urls = {
            'account_list': reverse('bank-accounts-api:account-list')
        }
        self.user = UserFactory()
        self.client.force_authenticate(self.user)

    def test_account_list_api_view(self):
        """
        Ensure API view will return list of accounts (contain required fields)
        that belong to authenticated user.
        """
        required_fields = [
            'id',
            'first_name',
            'last_name',
            'iban'
        ]
        another_user = UserFactory()
        another_account_list = AccountFactory.create_batch(5, manager=another_user)
        user_account_list = AccountFactory.create_batch(5, manager=self.user)
        user_account_id_list = [a.id for a in user_account_list]

        response = self.client.get(self.urls['account_list'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_account_id_list = []

        for account in response.data:
            self.assertListEqual(account.keys(), required_fields)
            response_account_id_list.append(account['id'])
        self.assertListEqual(user_account_id_list, response_account_id_list)

    def test_create_account_with_empty_data(self):
        """
        Ensure API view will return appropriate errors if empty data has been sent.
        """
        data = {}
        required_fields = [
            'first_name',
            'last_name',
            'iban'
        ]
        response = self.client.post(self.urls['account_list'], data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(required_fields, response.data.keys())

    def test_create_account_with_invalid_data(self):
        """
        Ensure API view will return appropriate errors if invalid data has been sent.
        """
        invalid_string = 'a' * 256
        data = {
            'first_name': invalid_string,
            'last_name': invalid_string,
            'iban': 'invalid'
        }
        response = self.client.post(self.urls['account_list'], data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(data.keys(), response.data.keys())

    def test_create_account_with_valid_data(self):
        """
        Ensure correct account will be created in DB.
        """
        data = {
            'first_name': 'Tony',
            'last_name': 'Stark',
            'iban': 'DE89370400440532013000'
        }
        response = self.client.post(self.urls['account_list'], data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_account = Account.objects.get(iban=data['iban'])
        for field_name, value in data.items():
            self.assertEqual(getattr(created_account, field_name), value)
        self.assertEqual(created_account.manager, self.user)

