from django import forms
from .models import HistoriaClinica
from ckeditor.widgets import CKEditorWidget

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'diagnostico']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'diagnostico': CKEditorWidget(attrs={'class': 'form-control'}),
        }
    
    medico = forms.CharField(
        label="Médico",
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )

    def __init__(self, *args, **kwargs):
        medico = kwargs.pop('medico', None)
        super().__init__(*args, **kwargs)
        if medico:
            self.fields['medico'].initial = medico.nombre  