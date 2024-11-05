from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, ComentarioForm, InicioSesionForm, FormularioContacto
from .models import Comentario, Contacto
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone

def inicio(request):
    if request.user.is_authenticated:
        contacto_form = FormularioContacto()
        registros = Contacto.objects.filter(usuario=request.user)  # Obtenemos los registros del usuario autenticado
    else:
        contacto_form = None
        registros = None
    # Maneja el formulario de inicio de sesión dentro del modal
    if request.method == 'POST' and 'loginForm' in request.POST:
        login_form = InicioSesionForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                login_form.add_error(None, 'Correo o contraseña incorrectos.')
    else:
        login_form = InicioSesionForm()
        
    # Formulario de registro
    register_form = RegistroUsuarioForm()
    
    # Formulario de contacto para usuarios autenticados
    contacto_form = FormularioContacto() if request.user.is_authenticated else None

    context = {
        'login_form': login_form,
        'register_form': register_form,
        'contacto_form': contacto_form,
        'registros': registros,
    }
    return render(request, 'inicio/inicio.html', context)

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'inicio/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']  # Obtiene el usuario autenticado de cleaned_data
            login(request, user)  # Inicia sesión con el usuario autenticado
            return redirect('inicio')  # Redirige a la página de inicio
    else:
        form = InicioSesionForm()
    return render(request, 'inicio/login.html', {'form': form})
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('inicio')  # Redirecciona a la página de inicio
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Has cerrado sesión exitosamente.")
        return super().dispatch(request, *args, **kwargs)

@login_required
def comentarios(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect('comentarios')
    else:
        form = ComentarioForm()
    comentarios = Comentario.objects.all()
    return render(request, 'inicio/comentarios.html', {'form': form, 'comentarios': comentarios})

@login_required
def editar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id, usuario=request.user)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('comentarios')
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'inicio/editar_comentario.html', {'form': form})

@login_required
def eliminar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id, usuario=request.user)
    comentario.delete()
    return redirect('comentarios')
# inicio/views.py
def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            # Obtén el usuario y la fecha actual
            Contacto.objects.create(
                usuario=request.user,  # Usuario autenticado
                nombre=form.cleaned_data['nombre'],
                edad=form.cleaned_data['edad'],
                color_favorito=form.cleaned_data['color_favorito'],
            )
            print("Registro guardado en la base de datos.")  # Confirmación de guardado
            return redirect('contacto')
        else:
            print(form.errors)  # Muestra los errores del formulario si no es válido

    else:
        form = FormularioContacto()

    registros = Contacto.objects.filter(usuario=request.user)

    return render(request, 'inicio/contacto.html', {'form': form, 'registros': registros})