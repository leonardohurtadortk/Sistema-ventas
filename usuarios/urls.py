from django.urls import path 
from .views import registro   

urlpatterns = [
    path("perfil/", registro , name="perfil"),
    ## el local cambiarlo por el nombre del local
  
]
