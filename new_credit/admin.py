from django.contrib import admin
from .models import Usuario, Divida


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
