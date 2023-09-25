from django.shortcuts import render

# Create your views here.


def inicio(request):
    ejemplo = "hola mundo"
    dof="cccyuyuyudddddd"
    return render (request,"inicio.html")