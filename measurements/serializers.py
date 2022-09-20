# TODO: опишите сериализаторы
from rest_framework.serializers import ModelSerializer
from measurements.models import Sensor, Measurement

class MeasurementSerializer(ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorSerializer(ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = '__all__'