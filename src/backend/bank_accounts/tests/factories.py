import factory

from core.tests.factories import UserFactory

from bank_accounts.models import Account


class AccountFactory(factory.DjangoModelFactory):
    manager = factory.SubFactory(UserFactory)

    class Meta:
        model = Account
