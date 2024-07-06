from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre","correo", "tipo_consulta", "mensaje", "avisos"]


# FORMS PARA CREAR UN PRODUCTO Y QUE SE GUARDEN SUS IMAGENES

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
