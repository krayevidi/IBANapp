from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'iban',
        'manager'
    )


admin.site.register(Account, AccountAdmin)
