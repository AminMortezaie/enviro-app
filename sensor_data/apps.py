from django.apps import AppConfig


class SensorDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensor_data'

    def ready(self):
        from sensor_data.mqtt.mqtt_client import start_mqtt
        start_mqtt()
