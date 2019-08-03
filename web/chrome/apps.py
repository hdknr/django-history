from django.apps import AppConfig


class ChromeConfig(AppConfig):
    name = 'chrome'

    def ready(self):
        from . import tasks  # NOQA