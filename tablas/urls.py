from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, LoteViewSet

# Crear el enrutador y registrar los ViewSets de Producto y Lote
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'lotes', LoteViewSet)

# Incluir las rutas registradas en urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
