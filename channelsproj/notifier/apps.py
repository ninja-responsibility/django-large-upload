from django.apps import AppConfig


class NotifierConfig(AppConfig):
    name = 'notifier'

    # ray test added
    def ready(self):
        from . import signals