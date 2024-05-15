from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    title = models.TextField(max_length=10)
    description = models.TextField(max_length=20)

class Measurement(models.Model):
    sensor_id = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    temperature = models.IntegerField()
    date_time = models.DateTimeField()
