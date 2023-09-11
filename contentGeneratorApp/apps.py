from django.apps import AppConfig


class ContentgeneratorappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contentGeneratorApp'



    def ready(self):
        import contentGeneratorApp.signals