from django import forms
from .models import Perfil
from .models import Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'email' : 'Correo',
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'password1' : 'Contraseña',
            'password2' : 'Confirme contraseña',
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form'}),
            'email' : forms.TextInput(attrs={'class':'form'}),
            'first_name': forms.TextInput(attrs={'class':'form'}),
            'last_name' : forms.TextInput(attrs={'class':'form'}),
            'password1' : forms.TextInput(attrs={'class':'form'}),
            'password2' : forms.TextInput(attrs={'class':'form'}),
        }




class AgregarProducto(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'nombreProducto',
            'precioProducto',
            'descripcion',
            'stockProducto',
            'fotoProducto',
        ]
        labels = {
            'nombreProducto' : 'Nombre de producto',
            'precioProducto' : 'Precio',
            'descripcion' : 'Descripción',
            'stockProducto' : 'Stock',
            'fotoProducto': 'Foto de producto',
        }
        widgets = {
            'nombreProducto' : forms.TextInput(attrs={'class':'form'}),
            'precioProducto' : forms.TextInput(attrs={'class':'form'}),
            'descripcion': forms.TextInput(attrs={'class':'form'}),
            'stockProducto' : forms.TextInput(attrs={'class':'form'}),
        }