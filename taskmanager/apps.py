from django.apps import AppConfig


class TaskmanagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "taskmanager"

    def ready(self):
        from . import signals




