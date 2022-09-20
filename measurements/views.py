from rest_framework.viewsets import ModelViewSet

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorViewSet(ModelViewSet):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
