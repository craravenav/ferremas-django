from django import forms
from .models import Contacto, Producto, Cliente, Marca, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre","correo", "tipo_consulta", "mensaje", "avisos"]


# FORMS PARA CREAR UN PRODUCTO Y QUE SE GUARDEN SUS IMAGENES

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    rut = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            cliente = Cliente(
                user=user,
                rut=self.cleaned_data['rut']
            )
            cliente.save()
        return user