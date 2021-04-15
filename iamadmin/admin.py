from django.contrib import admin

from iamadmin.models import Company, Subscriptions, Billing, Modules, Package

# Register your models here.
admin.site.register(Company)
admin.site.register(Subscriptions)
admin.site.register(Billing)
admin.site.register(Modules)
admin.site.register(Package)

