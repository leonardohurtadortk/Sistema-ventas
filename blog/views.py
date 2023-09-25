from django.shortcuts import render

# Create your views here.


def inicio(request):
    ejemplo = "hola mundo"
    dof="cccnnnnnnxxssxxxx"
    return render (request,"inicio.html")