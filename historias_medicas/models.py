from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from registro.models import Medico

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    diagnostico = RichTextField()

    def __str__(self):
        return f"Diagnostico de: {self.paciente.username} con el medico: {self.medico} el dia:  {self.fecha}"