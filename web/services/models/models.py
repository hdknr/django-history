from django.db import models
from . import defs


class GoogleKeep(defs.GoogleKeep):

    class Meta:
        verbose_name = 'Google Keep'
        verbose_name_plural = 'Google Keep'
