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
from historias_medicas.decorators import medico_required

@login_required
def lista_turnos(request):
    turnos = Turno.objects.filter(estado='D')
    return render(request, 'turnos/lista_turnos.html', {'turnos': turnos})

def reservar_turno(request):
    if request.method == "POST":
        medico_id = request.POST.get('medico')
        turno_id = request.POST.get('turno')
        
        if medico_id and turno_id:
            medico = Medico.objects.get(id=medico_id)
            cliente = request.user
            
            turno = Turno.objects.get(id=turno_id)
            
            if turno.estado == 'D':
                turno.cliente = cliente
                turno.estado = 'R'
                turno.save()
                return redirect('turno_reservado')
            else:
                return redirect('reservar_turno')
        else:
            return redirect('reservar_turno')
    
    medicos = Medico.objects.all()
    turnos_disponibles = {}
    for medico in medicos:
        turnos = Turno.objects.filter(estado='D', fecha__gte=timezone.now().date(), medico=medico)
        if turnos.exists():
            turnos_disponibles[medico.id] = list(turnos.values('id', 'fecha', 'hora_inicio'))

    return render(request, 'reservar_turno.html', {
        'medicos': medicos,
        'turnos_disponibles': turnos_disponibles
    })

def turno_reservado(request):
    return render(request, 'turno_reservado.html')

def turno_no_disponible(request):
    return render(request, 'turno_no_disponible.html')


@login_required
def cancelar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id, estado='R', cliente=request.user)
    turno.estado = 'C'
    turno.especialidad = None
    turno.save()
    return redirect('mis_turnos')

@login_required
def mis_turnos(request):
    turnos = Turno.objects.filter(cliente=request.user)
    return render(request, 'mis_turnos.html', {'turnos': turnos})

@login_required
@medico_required
def mis_turnos_medico(request):
    medico = Medico.objects.get(user=request.user)
    turnos = Turno.objects.filter(medico=medico, estado='R', fecha__gte=timezone.now())
    return render(request, 'mis_turnos_medico.html', {'turnos': turnos})

def generar_turnos(request):
    
    if request.user.is_superuser:

        fecha = datetime(2024, 6, 15).date()  # Ajustar la fecha
        crear_turnos(fecha)
        return HttpResponse("Turnos creados con éxito para la fecha especificada.")
    else:
        return redirect('login')

def get_turnos_disponibles(request):
    medico_id = request.GET.get('medico_id')
    turnos_disponibles = Turno.objects.filter(estado='D', fecha__gte=timezone.now().date(), medico_id=medico_id)
    data = [{'id': turno.id, 'fecha': turno.fecha, 'hora_inicio': turno.hora_inicio} for turno in turnos_disponibles]
    return JsonResponse(data, safe=False)
