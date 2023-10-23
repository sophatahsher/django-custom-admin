from django import apps


class AppConfig(apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'

    def read(self):
        from .health_checks import register_health_checks
        register_health_checks()
