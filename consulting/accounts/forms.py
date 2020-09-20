from django import forms
from .models import Doctor, Patient, TestUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class DoctorForm(forms.ModelForm):   
    
    class Meta:
        model = Doctor
        fields = ("curp", "cedula", "universidad", "date_birth", "tel_phone", "cel_phone", "sex", "age", "residence")
    

class PatientForm(forms.ModelForm):
    user = forms.CharField(label="usuario", max_length=150, required=False, widget=forms.HiddenInput())
    class Meta:
        model = Patient
        fields = ("user", "curp", "date_birth", "tel_phone", "cel_phone", "sex", "age", "residence")

    def clean_curp(self):
        data = self.cleaned_data["curp"]
        if len(data) < 10:
            raise ValidationError("Debe ser mayor de 10 números")
        return data
    


class TestUserForm(forms.ModelForm):
    name = forms.CharField(label="Nombre", max_length=100, required=False)

    class Meta:
        model = TestUser
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        super().__init__(*args, **kwargs)
        if self.initial:#Cuando se vaya a modificar será True
            print("Entramos aquí")
        else:#Si vas a crear se va aquí
            if TestUser.objects.filter().exists():
                testuser = TestUser.objects.filter(id=pk).values_list('name', flat=True)
                self.initial['name']=testuser.last()
            
