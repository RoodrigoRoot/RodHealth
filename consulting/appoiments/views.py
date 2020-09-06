from django.shortcuts import render
from django.views import View
from .forms import AppoimentsForm
# Create your views here.

class AppoimentView(View):
    
    def get(self, request, *args, **kwargs):
        form = AppoimentsForm()
        return render(request, 'appoiments/appoiments.html', locals())
