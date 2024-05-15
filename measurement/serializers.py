from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description']

class MeasurementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'date_time']
