from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import AppoimentsForm
from .models import Appoiments
# Create your views here.

class AppoimentsCreateView(CreateView):
    model = Appoiments
    form_class = AppoimentsForm
    success_url = reverse_lazy("index")
    template_name = "appoiments/appoiments.html"


class AppoimentsUpdateView(UpdateView):
    model = Appoiments
    form_class = AppoimentsForm
    success_url = reverse_lazy("index")
    template_name = "appoiments/update_appoiments.html"



    
