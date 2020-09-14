from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm
from django.contrib.auth import logout, authenticate, login

# Create your views here.

class IndexView(View):
    """Class of view Index
      Only show optios to doctor.""" 
      
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))
        return render(request, "core/index.html", locals())

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("index"))
        form = LoginForm()
        return render(request, "core/login.html", locals())
    
    
    def post(self, request, *args, **kwargs):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['passwd']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("index"))
        else:
            error = True
            form = LoginForm()
        return render(request, 'core/login.html', locals())