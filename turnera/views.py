from django.shortcuts import render
from .crear_turnos import crear_turnos
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from turnera.forms import TurnoForm
from django.urls import reverse
from .models import Turno, Medico

@login_required
def lista_turnos(request):
    turnos = Turno.objects.filter(estado='D')
    return render(request, 'turnos/lista_turnos.html', {'turnos': turnos})

'''@login_required
def reservar_turno(request):
    if request.method == "POST":
        form = TurnoForm(request.POST)
        if form.is_valid():
            turno = form.save(commit=False)
            turno.cliente = request.user
            turno.estado = 'R'
            turno.save()
            return redirect(reverse('turno_reservado'))
    else:
        form = TurnoForm()

    return render(request, 'reservar_turno.html', {'form': form})'''

def reservar_turno(request):
    if request.method == "POST":
        medico_id = request.POST['medico']
        turno_id = request.POST['turno']
        medico = Medico.objects.get(id=medico_id)
        cliente = request.user
        
        turno = Turno.objects.get(id=turno_id)
        
        if turno.estado == 'D':
            turno.cliente = cliente
            turno.estado = 'R'
            turno.save()
            return redirect('turno_reservado')
        else:
            return redirect('turno_no_disponible')
    
    medicos = Medico.objects.all()
    #turnos_disponibles = Turno.objects.filter(estado='D', fecha__gte=timezone.now().date())
    turnos_disponibles = {}
    for medico in medicos:
        turnos_disponibles[medico] = Turno.objects.filter(estado='D', fecha__gte=timezone.now().date(), medico=medico)

    #return render(request, 'reservar_turno.html', {'medicos': medicos, 'turnos_disponibles': turnos_disponibles})
    return render(request, 'reservar_turno.html', {'medicos': medicos, 'turnos_disponibles': turnos_disponibles})
'''
@login_required
def reservar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id, estado='D')
    turno.estado = 'R'
    turno.paciente = request.user
    turno.save()
    return redirect('lista_turnos')'''

def turno_reservado(request):
    return render(request, 'turno_reservado.html')

def turno_no_disponible(request):
    return render(request, 'turno_no_disponible.html')


@login_required
def cancelar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id, estado='R', cliente=request.user)
    turno.estado = 'D'
    turno.cliente = None
    turno.especialidad = None
    turno.save()
    return redirect('mis_turnos')

@login_required
def mis_turnos(request):
    turnos = Turno.objects.filter(cliente=request.user)
    return render(request, 'mis_turnos.html', {'turnos': turnos})

def generar_turnos(request):
    fecha = datetime(2024, 6, 5).date()  # Puedes ajustar la fecha según necesites
    crear_turnos(fecha)
    return HttpResponse("Turnos creados con éxito para la fecha especificada.")

def get_turnos_disponibles(request):
    medico_id = request.GET.get('medico_id')
    turnos_disponibles = Turno.objects.filter(estado='D', fecha__gte=timezone.now().date(), medico_id=medico_id)
    data = [{'id': turno.id, 'fecha': turno.fecha, 'hora_inicio': turno.hora_inicio} for turno in turnos_disponibles]
    return JsonResponse(data, safe=False)
