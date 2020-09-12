from django import forms
from .models import Appoiments
from accounts.models import Patient
from django.core.exceptions import ValidationError
class AppoimentsForm(forms.ModelForm):
    
    patient = forms.ModelChoiceField(label="Paciente", required=True, queryset=Patient.objects.all(), widget=forms.Select(attrs={
        "class":"select-patient"
    })
                                     )
    date = forms.DateTimeField(label="Fecha",
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    
    
    class Meta:
        model = Appoiments
        fields = ("doctor","patient","telefono", "date", "category")
    
    def clean_telefono(self):
        data = self.cleaned_data["telefono"]
        if len(str(data)) < 10:
            raise ValidationError("El teléfono no puede ser menor de 10 caracteres")
        return data
    