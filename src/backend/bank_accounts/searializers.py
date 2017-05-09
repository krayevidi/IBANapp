from rest_framework import serializers

from bank_accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'first_name',
            'last_name',
            'iban'
        ]
