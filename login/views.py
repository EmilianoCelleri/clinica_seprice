from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from login.forms import LoginForm
from django.contrib.auth import login, authenticate
# Create your views here.


def login_request(request):
    
    if request.method == 'POST':

        form=LoginForm(request, data=request.POST)
        if form.is_valid:
            usuario= request.POST['username']
            password= request.POST['password']

            usuario=authenticate(username=usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                return render (request, "index.html", {'form':form, 'mensaje': f"Bienvenido/a {usuario}"})
            else:
                return render (request, "login.html", {'form':form, 'mensaje': f"Usuario o clave incorrectos"})
        else:
            return render (request, "login.html", {'form':form, 'mensaje': f"Formulario invalido"})
    else:
        form = LoginForm()
        return render (request, "login.html", {'form':form})