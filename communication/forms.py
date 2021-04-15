from django import forms
from communication.models import Chat
from django.contrib.auth.models import User

class ChatForm(forms.ModelForm):
	class Meta():
		model = Chat
		fields = ('message',)
