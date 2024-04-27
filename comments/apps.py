from django.apps import AppConfig


class CommentsConfig(AppConfig):
    """
    AppConfig class for the comments app.
    
    This class defines configuration for the comments app, including the default_auto_field
    setting and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
