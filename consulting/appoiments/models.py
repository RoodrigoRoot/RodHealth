from django.db import models
from accounts.models import Doctor, Patient

# Create your models here.
class Appoiments(models.Model):
    CATEGORIES = (("General","General"),("Embarazo","Embarazo"),("Otra","Otra"))
    
    doctor = models.ForeignKey(Doctor, verbose_name=("Doctor"), on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, verbose_name=("Paciente"), on_delete=models.CASCADE)
    telefono = models.PositiveIntegerField(verbose_name=("Teléfono"))
    date = models.DateTimeField(verbose_name=("Fecha"), auto_now=False, auto_now_add=False)
    category = models.CharField(verbose_name=("Categoría"), max_length=50, choices=CATEGORIES)
    
    
    def __str__(self):
        return self.patient.user.username
    
    
    
    
    