from django.contrib import admin
from django.core.exceptions import ValidationError

from measurements.models import Sensor, Measurement


@admin.register(Sensor)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'latitude', 'longitude')
    list_display_links = ('id','name')

@admin.register(Measurement)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','temperature', 'sensor')
    list_display_links = ('id','value')

