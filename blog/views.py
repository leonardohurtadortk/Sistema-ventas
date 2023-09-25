from django.shortcuts import render

# Create your views here.


def inicio(request):
    ejemplo = "hola ndo"
    dof="c"
    return render (request,"inicio.html")