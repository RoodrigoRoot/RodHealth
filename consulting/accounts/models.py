from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
import uuid
from datetime import timedelta 
import datetime as dt
from django.shortcuts import reverse

# Create your models here.

class UserGeneral(models.Model):

    SEXOS = (("Femenino","Femenino"),
            ("Masculino","Masculino"))

    user = models.OneToOneField(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    date_birth = models.DateField(verbose_name=("Fecha de nacimiento"), auto_now=False, auto_now_add=False)
    residence = models.CharField(verbose_name="Residencia", max_length=255)
    tel_phone = models.CharField(verbose_name="Teléfono", blank=True, null=True, max_length=50)
    cel_phone = models.CharField(verbose_name="Celular", blank=True, null=True,max_length=50)
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
    
    def get_absolute_url(self):
        return reverse("account", kwargs={"pk": self.pk})
    
    
    

def set_slug(sender, instance, *args, **kwargs):
    user = instance.user.first_name
    last_name = instance.user.last_name
    uid = str(uuid.uuid4())[:4]
    slug = "{}-{}-{}".format(user, last_name, uid)
    instance.slug = slugify(slug)    

def set_age(sender, instance, *args, **kwargs):
    date = instance.date_birth.year
    year = int(dt.datetime.now().year)
    age = year - date
    instance.age = age

pre_save.connect(receiver=set_slug, sender=Doctor)   
pre_save.connect(receiver=set_age, sender=Doctor)
    
class Patient(UserGeneral):
    
    def __str__(self):
        return self.user.username

pre_save.connect(receiver=set_slug, sender=Patient)
pre_save.connect(receiver=set_age, sender=Patient)  