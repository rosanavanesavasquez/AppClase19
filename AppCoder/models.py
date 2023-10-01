from django.db import models

# Create your models here.


# En el archivo models.py de la aplicación AppCoder

from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.CharField(max_length=40)  

    #def __str__(self):
     #   return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    #def __str__(self):
     #   return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

   # def __str__(self):
    #    return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField(default=False)

  #  def __str__(self):
   #     return self.nombre


