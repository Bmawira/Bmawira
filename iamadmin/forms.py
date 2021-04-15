from django import forms
from django.contrib.auth.models import User

from iamadmin.models import Company

# Workstation form
class CompanyForm(forms.ModelForm):
	class Meta () :
		model = Company
		fields = ('company','address','phone','email',)
