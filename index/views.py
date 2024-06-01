from django.shortcuts import render

# Create your views here.


def index(request):
    # Retorna el index renderizado
    return render (request, "index.html")
