from django.apps import AppConfig


class AuthenticationServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication_service'

    def ready(self):
        print("authentication service is ready")
