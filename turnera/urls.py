from django.urls import path
from . import views

urlpatterns = [
    path('turnos/', views.lista_turnos, name='lista_turnos'),
    path('reservar_turno/', views.reservar_turno, name='reservar_turno'),
    path('cancelar/<int:turno_id>/', views.cancelar_turno, name='cancelar_turno'),
    path('mis_turnos/', views.mis_turnos, name='mis_turnos'),
    path('turno_reservado/', views.turno_reservado, name='turno_reservado'),
    path('generar_turnos/', views.generar_turnos, name='generar_turnos'),
    path('turno_no_disponible/', views.turno_no_disponible, name='turno_no_disponible'),
    path('get_turnos_disponibles/', views.get_turnos_disponibles, name='get_turnos_disponibles'),
]