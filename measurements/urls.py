from django.urls import path
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from measurements.views import SensorViewSet, MeasurementViewSet

router = SimpleRouter()
router.register('sensor', SensorViewSet)
router.register('measurement', MeasurementViewSet)

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('/v1/', include(router.urls)),
]
