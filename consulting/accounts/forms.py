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
        fields = ("user", "curp", "cedula", "universidad", "date_birth", "tel_phone", "cel_phone", "sex", "age")
    #username = forms.CharField(label="Usuario", help_text="Ingresa tu nombre de usuario", required=True)
    #passwd = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
        #attrs={
        #    "placeholder":"Ingresa tu contraseña"
        #}
    #))
    