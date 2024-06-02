from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Especialidad(models.Model):
    especialidad = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.especialidad
        

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.OneToOneField(Especialidad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre + " " + self.apellido
    

