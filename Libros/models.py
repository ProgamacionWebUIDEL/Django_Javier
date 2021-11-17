from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=120, help_text='title of message.')
    autor = models.CharField(max_length=120, help_text='autor of message.')
    numero_pag = models.IntegerField(help_text='Número de Páginas')
    isbn = models.CharField(max_length=20, help_text='Código de Barras')
    editorial = models.CharField(max_length=100, help_text='Editorial')

class Autos(models.Model):
    marca = models.CharField(max_length=200, help_text='Marca del Vehiculo')
    cilindraje = models.FloatField(help_text='Cilindraje')

class Computadoras(models.Model):
    marca = models.CharField(max_length=200, help_text='Marca del Computador')
    serie = models.CharField(max_length=200, help_text='Serie')
    precio = models.FloatField(max_length=200, help_text='Precio')

