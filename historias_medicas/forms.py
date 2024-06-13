from django import forms
from .models import HistoriaClinica
from ckeditor.widgets import CKEditorWidget

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'medico', 'diagnostico']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'diagnostico': CKEditorWidget(attrs={'class': 'form-control'}),
        }