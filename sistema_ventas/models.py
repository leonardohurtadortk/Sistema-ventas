from django.db import models

# Create your models here.


class Bebidas(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre

class Comida(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre

    
class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    disponible = models.BooleanField(default=True)
    class Meta:
        ordering = ["numero"]

    def total_mesa(self):
        return sum(pedido.total() for pedido in self.mesa_pedidos.filter(estado=False))        
    def __str__(self):
        return str(self.numero)

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, blank=True , null= True, related_name="mesa_pedidos")
    barra = models.BooleanField(default=False)
    bebida = models.ManyToManyField(Bebidas,blank=True , related_name="bebidas_pedidos")
    bebida_cantidad = models.IntegerField(default=0) 
    comida = models.ManyToManyField(Comida,blank=True)
    comida_cantidad = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    def costo_bebidas(self):

        return sum([b.precio * self.bebida_cantidad for b in self.bebida.all()])
    
    def costo_comida(self):
        return sum([c.precio * self.comida_cantidad for c in self.comida.all()])
    
    def total(self):
        return self.costo_bebidas() + self.costo_comida()

    def __str__(self):
        return "Pedido {}".format(self.id)
    

