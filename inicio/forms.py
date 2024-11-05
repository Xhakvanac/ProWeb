from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comentario
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils import timezone

class InicioSesionForm(forms.Form):
    email = forms.EmailField(label="Correo")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                # Busca el usuario por el campo de correo electrónico
                user = authenticate(username=User.objects.get(email=email).username, password=password)
            except User.DoesNotExist:
                user = None
            
            if user is None:
                raise forms.ValidationError("Correo o contraseña incorrectos.")
            cleaned_data['user'] = user  # Aquí establecemos el usuario en cleaned_data

        return cleaned_data
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Ingresa un correo electrónico válido.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=150, required=True)
    edad = forms.IntegerField(required=True)
    color_favorito = forms.ChoiceField(choices=[
        ('Rojo', 'Rojo'),
        ('Verde', 'Verde'),
        ('Azul', 'Azul'),
        ('Amarillo', 'Amarillo'),
        ('Naranja', 'Naranja'),
        ('Morado', 'Morado'),
    ])
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']  # Solo necesita el campo de contenido
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario aquí...'}),
        }

