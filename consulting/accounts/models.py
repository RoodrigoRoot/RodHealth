from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserGeneral(models.Model):

    SEXOS = (("Femenino","Femenino"),
            ("Masculino","Masculino"))

    user = models.OneToOneField(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    date_birth = models.DateField(verbose_name=("Fecha de nacimiento"), auto_now=False, auto_now_add=False)
    residence = models.CharField(verbose_name="Residencia", max_length=255)
    tel_phone = models.CharField(verbose_name="Teléfono", blank=True, null=True, max_length=50)
    tel_phone = models.CharField(verbose_name="Celular", blank=True, null=True,max_length=50)
    sex = models.CharField(verbose_name=("Sexo"), max_length=10, choices=SEXOS)
    curp = models.CharField(verbose_name=("Curp"), max_length=50)
    slug = models.SlugField(verbose_name=("Slug"))
    age = models.PositiveIntegerField(verbose_name="Edad")
    created = models.DateField(verbose_name=("Creado"), auto_now=False, auto_now_add=True)
    updated = models.DateField(verbose_name=("Actualizado"), auto_now=True, auto_now_add=False)
    
    class Meta:
        abstract = True
        ordering = ['-curp']
    
class Doctor(UserGeneral):
    
    cedula = models.CharField(verbose_name=("Cédula"), max_length=30)
    universidad = models.CharField(verbose_name="Universidad", max_length=250)
    
    def __str__(self):
        return self.user.username
        

class Patient(UserGeneral):
    
    def __str__(self):
        return self.user