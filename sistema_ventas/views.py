from django.shortcuts import render,redirect ,HttpResponse
from .models import Mesa,Pedido
from .form import Formulario_config,Formulario_pedidos,Formulario_bebida

from django.db import IntegrityError

# Create your views here.

# views.py
from django.db.models import Count

def sistema_inicio(request):
    # Usamos 'prefetch_related' para recuperar todos los pedidos relacionados con cada mesa en una sola consulta
    mesas = Mesa.objects.prefetch_related('mesa_pedidos').annotate(num_pedidos=Count('mesa_pedidos')).order_by('numero')

    num_mesas_ocupadas = mesas.filter(disponible=False).count()
    num_mesas_ocupada = mesas.filter(disponible=False)

   
    


    todos_completos = all(pedidos.estado for pedidoss in mesas for pedidos in pedidoss.mesa_pedidos.all())

 
    # Ahora, cuando accedemos a 'mesa.mesa_pedidos.all()', Django no necesita hacer una consulta adicional a la base de datos
    pedidos = [pedido for mesa in mesas for pedido in mesa.mesa_pedidos.all()]

    p_pendientes = len([pedido for pedido in pedidos if pedido.estado == False])
    p_dia = len([pedido for pedido in pedidos if pedido.estado == True])


    mesass = [pedido for pedido in pedidos if pedido.estado == False]
    print(mesass)

            
    """
    

        if all(pedido.estado for pedido in pedidos):
            print(f"Mesa {mesa.numero}: Todos los pedidos están en True.")
        elif all(not pedido.estado for pedido in pedidos):
            print(f"Mesa {mesa.numero}: Todos los pedidos están en False.")
        else:
            print(f"Mesa {mesa.numero}: Los pedidos tienen estados mixtos.")

    """


    estado_var = pedidos
    num_total_mesas = mesas.count()

    return render(request, "sistema_ventas.html", {
        "mesas": mesas,
        "pedidos":pedidos,
        "num_mesas_ocupadas": num_mesas_ocupadas,
        "num_total_mesas": num_total_mesas,
        "num_total_pedidos": len(pedidos),
        "p_pendientes": p_pendientes ,
        "p_dia": p_dia,
        "estado":todos_completos,
    })

def agregar_pedidos(request, mesa):
    mesa = Mesa.objects.get(numero=mesa)
    if request.method == "POST":
        form_mesas = Formulario_pedidos(request.POST )
        if form_mesas.is_valid():
            pedidos = form_mesas.save(commit=False)
            pedidos.mesa = mesa

            mesa.disponible = False

            mesa.save()
            pedidos.save()
            form_mesas.save_m2m()
            return redirect ("sistema")
    else:
        form_mesas = Formulario_pedidos()
    return render(request,"agregar_pedido.html" ,{
        "form_mesas":form_mesas,
    })

def cobrar_pedidos(request , mesa):
    mesas = Mesa.objects.get(numero=mesa)
    pedidos = Pedido.objects.filter(mesa=mesas)

    return render(request,"cobrar_pedido.html",{
        
        "pedidos": pedidos,
        "mesas":mesas
        })

### realizar pago para una ventana emergente
def realizar_cobro(request, mesa):
    mesas = Mesa.objects.prefetch_related("mesa_pedidos").get(numero=mesa)
    pedidos = mesas.mesa_pedidos.all()
    for pedido in pedidos:
        pedido.estado = True
        mesas.disponible = True
        mesas.save()

        pedido.save()
    return redirect('sistema')







def ver_detalles (request, mesa):
    mesas = Mesa.objects.prefetch_related("mesa_pedidos").get(numero=mesa)
    pedidos = mesas.mesa_pedidos.all()
    num_tota_pedidos = pedidos.count()
    return render(request,"ver_detalles.html" , {
        "pedidos": pedidos,
        "num_total_pedidos": num_tota_pedidos,
        "mesas":mesas
        
        })


















def configurar(request):

    formulario = Formulario_config
    return render (request,"configurar.html",{
    
        
        })

def configurar_mesas(request):
    mesas = Mesa.objects.all()
    num_mesas = mesas.count()
    if request.method == "POST":
        formulario = Formulario_config(request.POST)
        if formulario.is_valid():
            try:
                mesas.create(numero=request.POST["numero"])
                return redirect("configurar_mesas")
            except IntegrityError:
                error_message = "Ya existe una mesa con el número {}".format(request.POST["numero"])
                # Puedes pasar este mensaje de error a tu plantilla y mostrarlo en tu página HTML
                return render(request, 'configurar_mesas.html', {'error_message': error_message, "mesas":mesas, "num_mesas":num_mesas, "form":formulario})
      
    else:
        formulario = Formulario_config
    return render (request,"configurar_mesas.html",{
        "mesas":mesas,
        "num_mesas":num_mesas,
        "form":formulario,
        
        })

def eliminar (request,id):
    mesas = Mesa.objects.get(id=id)
    mesas.delete()
    return redirect("configurar_mesas")

