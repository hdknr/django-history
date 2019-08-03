from django.dispatch import receiver
from histories.signals import update_link
from . import models
from logging import getLogger
logger = getLogger()


@receiver(update_link)
def on_update_link(sender, instance=None, **kwargs):
    obj = instance and models.Urls.objects.filter(url=instance.url).first()
    if obj:
        instance.title = obj.title
        instance.save()