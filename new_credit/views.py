# from rest_framework import generics
# from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

from .serializers import DividaSerializer, UsuarioSerializer
from .models import Usuario, Divida


###########################################################
#  API
###########################################################

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class DividaViewSet(viewsets.ModelViewSet):
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer
