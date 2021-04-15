from django.contrib import admin
from frontoffice.models import Visitor,PostalReceive,Postaldispatch,Equiry,Phone_call_log,Complain,Complain_type,Reference,Purpose,Source

# Register your models here.
admin.site.register(Visitor)
admin.site.register(PostalReceive)
admin.site.register(Postaldispatch)
admin.site.register(Equiry)
admin.site.register(Phone_call_log)
admin.site.register(Complain)
admin.site.register(Source)
admin.site.register(Purpose)
admin.site.register(Reference)
admin.site.register(Complain_type)
