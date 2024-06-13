from django.urls import path
from login.views import login_request
from django.contrib.auth.views import LogoutView
from .views import cargar_diagnostico, lista_historias_clinicas, historia_clinica_detalle, diagnostico_confirmado



urlpatterns = [
   

    path('cargar_diagnostico/', cargar_diagnostico, name='cargar_diagnostico'),
    path('diagnostico_confirmado/', diagnostico_confirmado, name='diagnostico_confirmado'),
    path('lista_historias_clinicas/', lista_historias_clinicas, name='lista_historias_clinicas'),
    path('<int:pk>/', historia_clinica_detalle, name='historia_clinica_detalle'),

]


