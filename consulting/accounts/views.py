from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from .models import Doctor, Patient
from django.contrib.auth.models import User
from .forms import DoctorForm, UserForm, PatientForm
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import uuid
import datetime
# Create your views here.

class DoctorUpdateView(UpdateView):   
    """This class is for update a Doctor"""
    model = Doctor
    form_class = DoctorForm
    template_name = "accounts/update.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        """Set the form to update data from User model of Django"""
        context = super().get_context_data(**kwargs)
        context["second_form"] = UserForm
        return context
    
    def post(self, request, *args, **kwargs):
        """This methow override the method post.
        we obtain @username, @last_name and @last_name
        to update default the model User .
        """
        self.object = self.get_object()        
        user = User.objects.get(username=request.POST.get("username"))
        user.first_name =request.POST.get("first_name")
        user.last_name =request.POST.get("last_name")
        user.save()
        return super().post(request, *args, **kwargs)



class PatientsCreateView(View):
    """PatientCreateView. This class Create patients.
    Has a two methdos. GET and POST.
    """
    def get(self, request, *args, **kwargs):
        """This methos set two forms, the first form is to data from Patient.
        The second form is to data from User model to user of Patient
        """
        form = PatientForm()
        second_form = UserForm()
        return render(request, 'accounts/patients.html', locals())
    
        
    def post(self, request, *args, **kwargs):        
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            uid = str(uuid.uuid4())[:4]
            username = "{}-{}-{}".format(first_name, last_name, uid)
            user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password="password"
            )
            date_birth=request.POST.get("date_birth")
            date_birth = datetime.datetime.strptime(date_birth, '%Y-%m-%d')
            Patient.objects.create(
                user=user,
                curp=request.POST.get("curp"),
                sex=request.POST.get("sex"),
                age=request.POST.get("age"),
                date_birth=date_birth,
                tel_phone=request.POST.get("tel_phone"),
                cel_phone=request.POST.get("cel_phone"),
            )
            alert = True
        form = PatientForm()
        second_form = UserForm()
        return render(request, 'accounts/patients.html', locals())


class UpdatePatient(UpdateView):
    
    model = Patient
    form_class = PatientForm
    template_name = "accounts/update_patients.html"
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["second_form"] = UserForm
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()        
        user = User.objects.get(username=request.POST.get("username"))
        user.first_name=request.POST.get("first_name")
        user.last_name=request.POST.get("last_name")
        user.email=request.POST.get("email")
        user.save()
        return super().post(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))