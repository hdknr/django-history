from django.db import models
from . import methods


class GoogleKeep(models.Model, methods.GoogleKeep):
    account = models.CharField(
        'Account', max_length=100, null=True, blank=True, default=None)
    login_name = models.CharField('Login Name', max_length=100)
    login_password = models.CharField('Login Password', max_length=100)
    token = models.TextField('Token', null=True, blank=True, default=None)

    class Meta:
        abstract = True