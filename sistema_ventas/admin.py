from django.contrib import admin
from .models import Bebidas,Mesa,Comida,Pedido

# Register your models here.
admin.site.register(Bebidas)
admin.site.register(Mesa)
admin.site.register(Comida)
admin.site.register(Pedido)