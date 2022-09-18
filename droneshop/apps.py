from django.apps import AppConfig


class DroneshopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'droneshop'
    def ready(self):
        import droneshop.signals