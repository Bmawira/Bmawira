from django.contrib import admin
from pm.models import Workstation, CompanyProject, Boq, BoqItem, BoqSubItem

# Register your models here.
admin.site.register(Workstation)
admin.site.register(CompanyProject)
admin.site.register(Boq)
admin.site.register(BoqItem)
# admin.site.register(BoqMainItem)
admin.site.register(BoqSubItem)
