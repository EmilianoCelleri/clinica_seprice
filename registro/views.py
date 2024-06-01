from django.shortcuts import render
from registro.forms import RegistroForm
# Create your views here.


def register(request):

    if request.method=='POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render (request, "index.html", {'form':form, 'mensaje': f"Usuario creado con exito! {username}"})
    else:
        form = RegistroForm()
    return render (request, "registro.html", {'form':form})