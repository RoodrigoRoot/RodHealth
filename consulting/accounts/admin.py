from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("cedula", "user", "curp")
    list_filter = ("user__username", "user__first_name", "curp")

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("user", "curp", "tel_phone")
    search_fields = ("user", "curp")
    



