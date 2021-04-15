from django import forms

from frontoffice.models import Visitor
#from inventory.models import Brands

class VisitorForm(forms.ModelForm):
    class Meta():
        model=Visitor
        fields=('name','phone','id_card','no_of_persons','intime','outtime','note','document',)
