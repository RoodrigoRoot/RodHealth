from django import forms
from .models import Appoiments
from accounts.models import Patient

class AppoimentsForm(forms.ModelForm):
    
    patient = forms.ModelChoiceField(label="Paciente", required=True, queryset=Patient.objects.all(), widget=forms.Select(attrs={
        "class":"select-patient"
    })
                                     )
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    class Meta:
        model = Appoiments
        fields = ("doctor","patient","telefono", "date", "category")
    