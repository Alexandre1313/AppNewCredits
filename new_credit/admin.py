from django.contrib import admin
from .models import Usuario, Divida, Consulta


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'data_criacao',
        'data_modificacao',
        'usuario',
        'senha'
    ]


@admin.register(Divida)
class DividaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'data_criacao',
        'data_modificacao',
        'usuario',
        'data_vencimento',
        'divida'
    ]


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'id_usuario',
        'data_criacao',
        'data_modificacao'
    ]
