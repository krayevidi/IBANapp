from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from bank_accounts.models import Account
from bank_accounts.tests.factories import AccountFactory


class TestAccountAPIViewsUnauthorizedUser(APITestCase):
    def _test_api_calls(self, url, methods=None):
        """
        Ensure API call to given :url: returns 401 status code for given :methods:.
        """
        methods = methods or ['get', 'post', 'put', 'patch', 'delete']
        for method in methods:
            response = getattr(self.client, method)(url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_account_list_api_view(self):
        """
        Ensure account list API view inaccessible for unauthorized user.
        """
        url = reverse('bank-accounts-api:account-list')
        self._test_api_calls(url, methods=['get', 'post'])

    def test_account_detail_api_view(self):
        """
        Ensure account detail API view inaccessible for unauthorized user.
        """
        account = AccountFactory()
        self.assertTrue(Account.objects.filter(pk=account.pk).exists())
        url = reverse('bank-accounts-api:account-detail', kwargs={'pk': account.pk})
        self._test_api_calls(url)
