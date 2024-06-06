from django.utils import timezone
from datetime import datetime, time, timedelta
from .models import Medico, Turno, Especialidad

def crear_turnos(fecha):
    # Definir el inicio y fin del horario laboral
    hora_inicio = time(8, 0)
    hora_fin = time(20, 0)
    duracion_turno = timedelta(minutes=15)
    
    # Obtener todos los médicos
    medicos = Medico.objects.all()
    
    for medico in medicos:
        especialidad = medico.especialidad
        hora_actual = datetime.combine(fecha, hora_inicio)
        hora_fin_datetime = datetime.combine(fecha, hora_fin)
        
        while hora_actual < hora_fin_datetime:
            # Verificar si el turno ya existe
            if not Turno.objects.filter(medico=medico, fecha=fecha, hora_inicio=hora_actual.time()).exists():
                Turno.objects.create(
                    medico=medico,
                    especialidad=especialidad,
                    fecha=fecha,
                    hora_inicio=hora_actual.time(),
                    duracion=duracion_turno,
                    estado='D'
                )
            hora_actual += duracion_turno