from django.db import models
from django.conf import settings

from localflavor.generic.models import IBANField


class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    iban = IBANField()

    manager = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return str('{} {}'.format(self.first_name, self.last_name))
