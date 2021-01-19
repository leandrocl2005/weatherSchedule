from django.apps import AppConfig


class WeatherConfig(AppConfig):
    name = 'weather'

    def ready(self):
        from weatherUpdater import updater
        updater.start()
