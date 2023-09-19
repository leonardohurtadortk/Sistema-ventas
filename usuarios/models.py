from django.db import models
from django.contrib.auth.models import User

# Create your models here.

            
class Perfil (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100,null=True)
    apellido = models.CharField(max_length=100,null=True)