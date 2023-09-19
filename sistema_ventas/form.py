from django import forms
from .models import Mesa, Bebidas, Comida,Pedido


class Formulario_config(forms.Form):
    numero = forms.IntegerField(min_value=0)


class Formulario_pedidos(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["comida","comida_cantidad","bebida","bebida_cantidad"]
    def clean(self):
        cleaned_data = super().clean()
        comida = cleaned_data.get("comida")
        bebida = cleaned_data.get("bebida")
        cantidad_comida = cleaned_data.get("comida_cantidad")
        cantidad_bebida = cleaned_data.get("bebida_cantidad")
        print(bool(comida))
        print(bool(bebida))
 
        if bool(comida) and bool(cantidad_comida) and not bool(bebida) and not bool(cantidad_bebida) or bool(bebida) and bool(cantidad_bebida) and not bool(comida) and not bool(cantidad_comida) or bool(comida) and bool(cantidad_comida) and bool(bebida) and bool(cantidad_bebida):
            return cleaned_data
        else:
            raise forms.ValidationError("Los campos no cumplen con la validación requerida. Debe completar el campo1 y el campo2, o el campo3 y el campo4, o todos los campos.")
##           self.add_error("comida_cantidad" ,"debes poner al menos una cantidad")



class Formulario_bebida(forms.ModelForm):
    class Meta:
        model = Bebidas
        fields = ["nombre", "cantidad"]