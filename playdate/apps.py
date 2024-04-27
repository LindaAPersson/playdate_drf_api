from django.apps import AppConfig


class PlaydateConfig(AppConfig):
    """
    Configuration class for the Playdate app.

    Attributes:
        default_auto_field (str): The name of the default auto field.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playdate'
