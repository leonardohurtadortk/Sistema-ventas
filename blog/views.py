from django.shortcuts import render

# Create your views here.


def inicio(request):
    ejemplo = "hola munddddo"
    dof="ccc"
    return render (request,"inicio.html")