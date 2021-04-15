from django.contrib.auth.models import User
from django import forms

from outpatients.models import Patient,VitalInfo,Treatment,PatCategory

class PatientForm(forms.ModelForm):
    class Meta():
        model=Patient
        fields=('pat_no','card_no','firstname','lastname','age','gender','contact','location','email','card_charges','pat_cat','blood_group', 'marital_status', 'known_allergy', 'kin','kin_relationship', 'kin_contact','admitted_by', 'casulty', 'old_patient', 'insurance', 'credit_limit', 'bed_group', 'bed_no','discharged',)

class VitalForm(forms.ModelForm):
    class Meta():
        model=VitalInfo
        fields=('patient','temperature','bp','pr','rr','weight','height',)

class TreatmentForm(forms.ModelForm):
    class Meta():
        model=Treatment
        fields=('complains','history','examination','lab_investigation','doc_notes','diagnosis',)

class PatCategoryForm(forms.ModelForm):
    class Meta():
        model=PatCategory
        fields=('category','description',)
