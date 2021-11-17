from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LibroSerializable
from .serializers import AutosSerializable
from .serializers import ComputadorasSerializable
from .models import Libro
from .models import Autos
from .models import Computadoras
# Create your views here.

class LibroVista(viewsets.ModelViewSet):
    serializer_class:LibroSerializable
    queryset=Libro.objects.all()

class AutosVista(viewsets.ModelViewSet):
    serializer_class:AutosSerializable
    queryset=Autos.objects.all()

class Computadoras(viewsets.ModelViewSet):
    serializer_class:ComputadorasSerializable
    queryset=Computadoras.objects.all()