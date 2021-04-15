from django import forms
from django.contrib.auth.models import User

from pm.models import Workstation
from fleet.models import FuelReserveRefill, FleetType, FleetCategory, FuelReserve, Machinery, FuelIssue


# fleet category
class FleetCategoryForm(forms.ModelForm):
	class Meta():
		model = FleetCategory
		fields = ('category',)


# Fleet types
class FleetTypeForm(forms.ModelForm):
	class Meta():
		model = FleetType
		fields = ('fleet_type',)


# Machinery
class MachineryForm(forms.ModelForm):
	class Meta():
		model = Machinery
		fields = ('reg','vmodel','insurance_expiry','inspection_date','insurance_scan',)


# fuel issue
class FuelIssueForm(forms.ModelForm):
	class Meta():
		model = FuelIssue
		fields = ('quantity', 'ordometer', 'route', 'work_hours')


# fuel issue
class FuelRecieptForm(forms.ModelForm):
	class Meta():
		model = FuelIssue
		fields = ('amount', 'reciept', 'ordometer', 'route', 'work_hours', 'supplier')


# fuel reserves
class FuelReserveForm(forms.ModelForm):
	class Meta():
		model = FuelReserve
		fields = ('reserve_name','capacity',)


class FuelReserveRefillForm(forms.ModelForm):
	class Meta:
		model = FuelReserveRefill
		fields = ('amount', 'unit_price')
