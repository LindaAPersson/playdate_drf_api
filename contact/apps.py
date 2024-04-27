from django.apps import AppConfig

class ContactConfig(AppConfig):
    """
    Configuration for the contact app.

    Attributes:
        default_auto_field (str): The default auto field for the app's models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
