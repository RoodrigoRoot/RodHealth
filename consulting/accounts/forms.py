from django import forms
from .models import Doctor, Patient
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class DoctorForm(forms.ModelForm):   
    
    class Meta:
        model = Doctor
        fields = ("curp", "cedula", "universidad", "date_birth", "tel_phone", "cel_phone", "sex", "age")
    

    