from django import forms
from .models import Doctor, Patient
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class DoctorForm(forms.ModelForm):   
    
    class Meta:
        model = Doctor
        fields = ("curp", "cedula", "universidad", "date_birth", "tel_phone", "cel_phone", "sex", "age", "residence")
    

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ("curp", "date_birth", "tel_phone", "cel_phone", "sex", "age", "residence")

    