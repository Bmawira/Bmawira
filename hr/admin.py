from django.contrib import admin
from django.db.models import Count, Sum
from hr.models import Employee, EmployeeType, LeaveCategory, Leave, Attendance, JobTitle


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_number', 'phone', 'job_title', 'workstation')
    # list_filter = ('workstation__project', 'workstation')
    date_hierarchy = 'employment_date'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.eprofile.company)


# Register your models here.
admin.site.register(EmployeeType)
admin.site.register(Leave)
admin.site.register(LeaveCategory)
admin.site.register(Attendance)
admin.site.register(JobTitle)


