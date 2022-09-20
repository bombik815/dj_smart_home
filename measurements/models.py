from django.db import models


class TimestampFields(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sensor(TimestampFields):
    """Объект на котором проводят измерения."""
    name = models.TextField()
    description = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Measurement(TimestampFields):
    """Измерение температуры"""
    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    nullable = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return '{0}_{1}'.format(self.temperature, self.sensor)
