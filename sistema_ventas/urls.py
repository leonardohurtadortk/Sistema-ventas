from django.urls import path    
from .views import sistema_inicio,ver_detalles,configurar,configurar_mesas, eliminar,agregar_pedidos,cobrar_pedidos ,realizar_cobro


urlpatterns = [
    path("", sistema_inicio, name="sistema"),
    path("configurar/", configurar , name="configurar"),
    path("configurar/mesas/", configurar_mesas , name="configurar_mesas"),
    path("eliminar/<int:mesa>", eliminar, name="eliminar"),
    path("agregar/mesa/<int:mesa>", agregar_pedidos, name="agregar_pedidos"),
    path ("cobrar/mesa/<int:mesa>" , cobrar_pedidos,name="cobrar_pedidos"),
    path ("realizar_cobro/mesa/<int:mesa>" , realizar_cobro,name="realizar_cobro"),



    path("detalles/mesa/<int:mesa>/", ver_detalles, name= "ver_detalles")
]
