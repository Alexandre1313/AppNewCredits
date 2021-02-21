from rest_framework.routers import SimpleRouter
from .views import DividaViewSet, UsuarioViewSet, ConsultasViewSet

router = SimpleRouter()

router.register('usuarios', UsuarioViewSet)
router.register('dividas', DividaViewSet)
router.register('consultas', ConsultasViewSet)
