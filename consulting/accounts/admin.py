from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("pk","cedula", "user", "curp")
    list_filter = ("user__username", "user__first_name", "curp")

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("pk","user", "curp", "tel_phone")
    search_fields = ("user", "curp")

@admin.register(TestUser)
class TestUserAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name") 

