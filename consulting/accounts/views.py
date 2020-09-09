from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.edit import UpdateView
from .models import Doctor
from django.contrib.auth.models import User
from .forms import DoctorForm, UserForm
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse_lazy
# Create your views here.

class MyAccountView(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.username
        doctor = Doctor.objects.get(user__username = user_id)
        form = DoctorForm()
        return render(request, 'accounts/update.html', locals())

    def post(self, request, *args, **kwargs):
        print(request.POST)
        try:        
            d = {
                'curp': [request.POST.get('curp')],
                'universidad': [request.POST.get('universidad')],
                'cedula':[request.POST.get('cedula')],
                'tel_phone':[request.POST.get('tel_phone')],
                'cel_phone':[request.POST.get('cel_phone')],
                'age':[request.POST.get('age')],
                #'sex':[request.POST['sex']],
                'date_birth':[request.POST.get('date_birth')],
                'residence':[request.POST.get('residence')]
            }   
            print(d) 
            form = DoctorForm(d)
            if form.is_valid():
                print("Valido")
        except Exception as e:
            print("error", e)
        return render(request, 'accounts/myaccount.html', locals())


class UpdateUser(UpdateView):   

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["second_form"] = UserForm()
       return context
    
    model = Doctor
    form_class = DoctorForm
    template_name = "accounts/update.html"
    success_url = reverse_lazy('index')


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))