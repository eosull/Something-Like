from django.apps import AppConfig


# Configuring blog app
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
