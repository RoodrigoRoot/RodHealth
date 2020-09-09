from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from .forms import AppoimentsForm
from django.contrib import messages
from .models import Appoiments
from accounts.models import Patient
# Create your views here.

class AppoimentsCreateView(CreateView):
    model = Appoiments
    form_class = AppoimentsForm
    success_url = reverse_lazy("index")
    template_name = "appoiments/appoiments.html"
    


    
