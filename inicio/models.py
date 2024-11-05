from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username}'


class Contacto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()
    color_favorito = models.CharField(max_length=20)
    fecha_captura = models.DateTimeField(auto_now_add=True)  # Guarda automáticamente la fecha y hora de creación

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"

