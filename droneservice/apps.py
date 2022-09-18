from django.apps import AppConfig


class DroneserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'droneservice'
    def ready(self):
        import droneservice.signals