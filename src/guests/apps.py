from django.apps import AppConfig


class GuestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.guests'
    verbose_name = "Гости Мероприятия"
