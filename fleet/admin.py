from django.contrib import admin
from fleet.models import FleetType, FleetCategory, Machinery

# Register your models here.

admin.site.register(FleetCategory)
admin.site.register(FleetType)
admin.site.register(Machinery)
