from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField("Título", max_length=150)
    descripcion = models.TextField("Descripción", blank=True, null=True)
    fecha_limite = models.DateField("Fecha límite", null=True, blank=True)
    completada = models.BooleanField("Completada", default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')

    creado_en = models.DateTimeField("Creado en", auto_now_add=True)
    actualizado_en = models.DateTimeField("Actualizado en", auto_now=True)

    class Meta:
        ordering = ['completada', 'fecha_limite', '-creado_en']
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return f"{self.titulo} ({'Completada' if self.completada else 'Pendiente'})"

    def esta_vencida(self):
        if self.fecha_limite:
            return self.fecha_limite < timezone.now().date() and not self.completada
        return False