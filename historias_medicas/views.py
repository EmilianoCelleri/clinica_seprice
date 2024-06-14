from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HistoriaClinica, User, Medico
from .forms import HistoriaClinicaForm
from .decorators import medico_required

@login_required
@medico_required
def cargar_diagnostico(request):
    medico = Medico.objects.get(user=request.user)
    pacientes = User.objects.filter(is_staff=False)

    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST, medico=medico)
        if form.is_valid():
            historia_clinica = form.save(commit=False)
            historia_clinica.medico = medico
            historia_clinica.save()
            return redirect('diagnostico_confirmado')
    else:
        form = HistoriaClinicaForm(medico=medico)

    return render(request, 'cargar_diagnostico.html', {'form': form, 'pacientes': pacientes})

@login_required
@medico_required
def lista_historias_clinicas(request):
    paciente_id = request.GET.get('paciente')
    historias_clinicas = HistoriaClinica.objects.all()

    if paciente_id:
        historias_clinicas = historias_clinicas.filter(paciente_id=paciente_id)

    pacientes = User.objects.filter(is_staff=False)

    context = {
        'historias_clinicas': historias_clinicas,
        'pacientes': pacientes,
    }
    return render(request, 'lista_historias_clinicas.html', context)

@login_required
@medico_required
def historia_clinica_detalle(request, pk):
    historia_clinica = HistoriaClinica.objects.get(pk=pk)
    return render(request, 'historia_clinica_detalle.html', {'historia_clinica': historia_clinica})

def diagnostico_confirmado(request):
    return render(request, 'diagnostico_confirmado.html')

def permiso_denegado(request):
    return render(request, 'permiso_denegado.html')

def mi_historia_clinica(request):
    historias_clinicas = HistoriaClinica.objects.filter(paciente=request.user)
    return render(request, 'mi_historia_clinica.html', {'historias_clinicas': historias_clinicas})



