from django.urls.base import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from core.tests.mixins import HTTPMethodStatusCodeTestMixin
from bank_accounts.tests.factories import AccountFactory


class TestAccountAPIViewsUnauthorizedUser(HTTPMethodStatusCodeTestMixin,
                                          APITestCase):
    def test_account_list_api_view(self):
        """
        Ensure account list API view inaccessible for unauthorized user.
        """
        self.run_method_status_code_check(
            url=reverse('bank-accounts-api:account-list'),
            methods=['get', 'post'],
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    def test_account_detail_api_view(self):
        """
        Ensure account detail API view inaccessible for unauthorized user.
        """
        account = AccountFactory()
        self.run_method_status_code_check(
            url=reverse('bank-accounts-api:account-detail',
                        kwargs={'pk': account.pk}),
            methods=['get', 'post', 'put', 'delete'],
            status_code=status.HTTP_401_UNAUTHORIZED
        )
