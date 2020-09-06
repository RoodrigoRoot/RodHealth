from django import forms
from .models import Appoiments

class AppoimentsForm(forms.ModelForm):
    
    class Meta:
        model = Appoiments
        fields = "__all__"
