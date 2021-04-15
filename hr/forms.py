from django import forms
from hr.models import Employee, Leave
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
	class Meta () :
		model = Employee
		fields = ('firstname', 'lastname', 'id_number', 'phone', 'email', 'gender', 'dob', 'account_number', 'basic_pay', 'kra_pin', 'nhif', 'nssf', 'dl_expiry', 'address', 'workstation', 'kin_name', 'kin_phone', 'driver_license', 'leaves', 'kin_relationship', 'expiry_date',)

class LeaveRequestForm(forms.ModelForm):
	class Meta():
		model = Leave
		fields = ('startdate', 'enddate', 'request_notes',)
