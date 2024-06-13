from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HistoriaClinica, User, Medico
from .forms import HistoriaClinicaForm

@login_required
def cargar_diagnostico(request):
    pacientes = User.objects.filter(is_staff=False)

    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            historia_clinica = form.save(commit=False)
            
            # Asignar el médico basado en el usuario actual
            medico = Medico.objects.get(user=request.user)
            historia_clinica.medico = medico
            
            historia_clinica.save()
            return redirect('diagnostico_confirmado')

    else:
        form = HistoriaClinicaForm()

    return render(request, 'cargar_diagnostico.html', {'form': form, 'pacientes': pacientes})

@login_required
def lista_historias_clinicas(request):
    historias_clinicas = HistoriaClinica.objects.filter(medico=request.user.medico)
    return render(request, 'lista_historias_clinicas.html', {'historias_clinicas': historias_clinicas})

@login_required
def historia_clinica_detalle(request, pk):
    historia_clinica = HistoriaClinica.objects.get(pk=pk)
    return render(request, 'historia_clinica_detalle.html', {'historia_clinica': historia_clinica})

def diagnostico_confirmado(request):
    return render(request, 'diagnostico_confirmado.html')