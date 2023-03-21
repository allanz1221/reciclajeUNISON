from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
    departamento = models.CharField(max_length=200)
    
    def __str__(self):
        return self.departamento


class Tipo(models.Model):
    tipo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tipo


class Material(models.Model):
    material = models.CharField(max_length=200)
    
    def __str__(self):
        return self.material


class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    completo_fecha = models.DateTimeField(auto_now_add=True)
    
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reciclaje de {str(self.material)}, {str(self.cantidad)} {self.tipo.tipo} por el Departamento de {self.departamento.departamento} Fecha: {self.creado.strftime('%d-%m-%Y')}."

        #return " "+ + " " + str(self.cantidad) + " " + self.tipo.tipo + " por el Departamento de " + self.departamento.departamento + " :: "+ str(self.creado)

    class Meta:
        ordering = ['completo']