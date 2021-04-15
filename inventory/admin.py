from django.contrib import admin
from inventory.models import Category,Brands,Uom,Items

# Register your models here.
admin.site.register(Category)
admin.site.register(Brands)
admin.site.register(Uom)
admin.site.register(Items)
