from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Editorial(models.Model):

    nombre=models.CharField(max_length=40)
    direccion = models.CharField(max_length=200)
    responsable = models.CharField(max_length=100)
    email= models.EmailField()


    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class Libro(models.Model):
    titulo= models.CharField(max_length=30)
    isbn= models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    publication_date = models.DateField()
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

