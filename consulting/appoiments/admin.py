from django.contrib import admin
from .models import Appoiments
# Register your models here.
class AppoimentAdmin(admin.ModelAdmin):
    list_display = ("pk", "doctor", "patient", "date", "category")


admin.site.register(Appoiments, AppoimentAdmin)