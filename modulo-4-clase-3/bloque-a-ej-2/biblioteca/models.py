from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    models.DateTimeField()


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    autores = models.ManyToManyField(Autor)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)


class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
