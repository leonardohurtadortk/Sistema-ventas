from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def registro(request):
    if request.method == 'GET':
        return render(request, "registro.html", {
            "form": UserCreationForm
        })
    else:
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if not password1 or not password2:
            return render(request, "registro.html", {
                "form": UserCreationForm,
                "error": "La contraseña es obligatoria"
            })
        elif password1 == password2:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=password1)
                user.save()
                login(request, user)
                return redirect("/")
            except:
                return render(request, "registro.html", {
                    "form": UserCreationForm,
                    "error": "El usuario ya existe"
                })
        else:
            return render(request, "registro.html", {
                "form": UserCreationForm,
                "error": "Las contraseñas no coinciden"
            })
