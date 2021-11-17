from rest_framework import serializers
from .models import Libro
from .models import Autos
from .models import Computadoras

class LibroSerializable(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields=(
            'titulo',
            'autor',
            'numero_pag',
            'isbn',
            'editorial'

        )

class AutosSerializable(serializers.ModelSerializer):
    class Meta:
        model = Autos
        fields=(
            'marca',
            'cilindraje'
        )

class ComputadorasSerializable(serializers.ModelSerializer):
    class Meta:
        model = Computadoras
        fields=(
            'marca',
            'serie',
            'precio'
        )