from django.db import models
from django.contrib.auth.models import User
from registro.models import Medico, Especialidad
from django.utils import timezone
# Create your models here.

class Turno(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    duracion = models.DurationField(default=timezone.timedelta(minutes=15))
    
    ESTADO_CHOICES = [
        ('D', 'Disponible'),
        ('R', 'Reservado'),
        ('C', 'Cancelado'),
    ]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='D')

    def __str__(self):
        return f"Turno de {self.medico} con {self.cliente} El dia: {self.fecha} a las: {self.hora_inicio}"

    class Meta:
        unique_together = ('medico', 'fecha', 'hora_inicio')
