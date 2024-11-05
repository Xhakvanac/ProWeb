from django.urls import path
from .views import CustomLogoutView
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('comentarios/editar/<int:id>/', views.editar_comentario, name='editar_comentario'),
    path('comentarios/eliminar/<int:id>/', views.eliminar_comentario, name='eliminar_comentario'),
    path('contacto/', views.contacto, name='contacto'),
]
