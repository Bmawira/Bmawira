from django import forms
from django.contrib.auth.models import User

from pm.models import Workstation, CompanyProject, Boq, BoqItem, BoqSubItem


# Workstation form
class WorkstationForm(forms.ModelForm):
	class Meta:
		model = Workstation
		fields = ('workstation', 'location',)


# project
class ProjectForm(forms.ModelForm):
	class Meta:
		model = CompanyProject
		fields = ('title',)


class BoqForm(forms.ModelForm):
	class Meta:
		model = Boq
		fields = ('title', 'sub_title', 'contract_no')


class BoqItemForm(forms.ModelForm):
	class Meta:
		model = BoqItem
		fields = ('description',)


class BoqSubItemForm(forms.ModelForm):
	class Meta:
		model = BoqSubItem
		fields = ('quantity', 'unit', 'rate', 'description',)

