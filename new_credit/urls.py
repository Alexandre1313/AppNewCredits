from rest_framework.routers import SimpleRouter
from .views import DividaViewSet, UsuarioViewSet

router = SimpleRouter()

router.register('usuarios', UsuarioViewSet)
router.register('dividas', DividaViewSet)
