from django.contrib import admin
from .models import HistoriaClinica
# Register your models here.

class HistoriasClinicasAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'fecha', 'diagnostico')
    readonly_fields=('fecha')

admin.site.register(HistoriaClinica)