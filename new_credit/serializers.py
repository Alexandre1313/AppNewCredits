from rest_framework import serializers
from .models import Usuario, Divida, Consulta


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'data_criacao',
            'data_modificacao',
            'usuario',
            'senha'
        )


class DividaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divida
        fields = (
            'id',
            'data_criacao',
            'data_modificacao',
            'usuario',
            'data_vencimento',
            'divida'
        )


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = (
            'id',
            'data_criacao',
            'data_modificacao'
        )
