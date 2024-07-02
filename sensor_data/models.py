from django.db import models

class SensorData(models.Model):
    hub_id = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hub_id} - {self.created_at}"
