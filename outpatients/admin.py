from django.contrib import admin

from outpatients.models import Patient,VitalInfo,Treatment,PatCategory

# Register your models here.
admin.site.register(Patient)
admin.site.register(VitalInfo)
admin.site.register(Treatment)
admin.site.register(PatCategory)
