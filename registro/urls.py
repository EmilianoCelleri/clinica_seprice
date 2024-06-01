from django.urls import path
from registro.views import register


urlpatterns = [
   
    path('registro/', register, name="registro"),

    


]