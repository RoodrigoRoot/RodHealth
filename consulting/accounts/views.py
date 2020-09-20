from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Doctor, Patient, TestUser
from .forms import DoctorForm, UserForm, PatientForm, TestUserForm
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import uuid
import datetime
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import model_to_dict
# Create your views here.

#Doctor

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "accounts/doctor.html"

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
        print(context)
        return context
    
    def post(self, request, *args, **kwargs):
        """This methow override the method post.
        we obtain @username, @last_name and @last_name
        to update default the model User .
        """
        self.object = self.get_object()        
        print(request.user.id)
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()
        return super().post(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))


#Patients
class PatientListView(ListView):
   model = Patient
   template_name="accounts/patients.html"



class PatientUpdateView(UpdateView):
    
    model = Patient
    form_class = PatientForm
    template_name = "accounts/update_patients.html"
    success_url = reverse_lazy('list_patients')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["second_form"] = UserForm
        return context

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    @property
    def pk(self):
        return self.kwargs["pk"]
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            User.objects.filter(patient=int(self.pk)).update(
                last_name=request.POST.get("last_name"),
                first_name=request.POST.get("first_name"))
            form = self.get_form()
            data = model_to_dict(form.save())
        except Exception as e:
            data['errors'] = str(e)
        return JsonResponse(data)        


   
   
class PatientsCreateView(CreateView):
    """PatientCreateView. This class Create patients.
    Has a two methdos. GET and POST.
    """
    model = Patient
    template_name = 'accounts/create_patients.html'
    form_class = PatientForm
    success_url = reverse_lazy("users:list_patients")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["second_form"] = UserForm()
        return context   

    def post(self, request, *args, **kwargs):
        data = {}
        user = None
        try:        
            user_form = UserForm(request.POST)
            patient_form = PatientForm(request.POST)
            if user_form.is_valid():
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name").split()[0]
                uid = str(uuid.uuid4())[:4]
                username = "{}-{}-{}".format(first_name, last_name, uid)
                user = user_form.save(commit=False)
                user.username = username
                user.save()
                user_form.save()
                if patient_form.is_valid():
                    patient = patient_form.save(commit=False)
                    patient.user=user
                    patient.save()
                    #print(patient_form.errors)
                    data = model_to_dict(patient_form.save())
                else:
                    print(patient_form.errors.get_json_data)
                    data['errors'] = patient_form.errors
        except Exception as e:
            print(e)
            data['errors'] = str(e)
        return JsonResponse(data)


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "accounts/delete_patients.html"
    success_url = reverse_lazy("list_patients")


class PatientDetailView(DetailView):
    model = Patient
    template_name = "accounts/detail_patient.html"


class TestUserFormView(CreateView):
    model = TestUser
    template_name = 'accounts/test.html'
    form_class = TestUserForm
    success_url = reverse_lazy("list_patients")

    def get_form_kwargs(self):
        kwargs = super(TestUserFormView, self).get_form_kwargs()
        kwargs['pk'] = self.request.GET['pk']
        return kwargs


    def post(self, request, *args, **kwargs):
        try:
            print(request.POST)
        except Exception as e:
            print(e)

class TestUserFormUpdateView(UpdateView):
    model = TestUser
    template_name = 'accounts/test.html'
    form_class = TestUserForm
    success_url = "/"

    #def get(self, request, *args, **kwargs):
        #form = TestUserForm()
    #    return render(request, 'accounts/test.html', locals())

    def post(self, request, *args, **kwargs):
        try:
            print(request.POST)
        except Exception as e:
            print(e)


class TestUserBase(CreateView):
    
    model = User
    form_class = UserCreationForm 
    template_name= "accounts/test.html"
    success_url = reverse_lazy("list_patients")
