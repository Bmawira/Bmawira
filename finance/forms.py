from django import forms
from django.contrib.auth.models import User

from finance.models import PettyCash


# fleet category
class PettyCashForm(forms.ModelForm):
	class Meta:
		model = PettyCash
		fields = ('amount',)
