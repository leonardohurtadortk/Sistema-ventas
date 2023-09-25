from django.shortcuts import render

# Create your views here.


def inicio(request):
    ejemplo = "ho"
    dof="ccc"
    return render (request,"inicio.html")