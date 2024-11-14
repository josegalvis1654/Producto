from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, LoteViewSet, ObtenerProductoView,ObtenerUbicacionView,ObtenerProveedorView,ObtenerCantidadTotalPorProductoView,LotesProximosACaducarView,LoteMasRecienteView,UbicacionViewSet,TipoViewSet,EstadoViewSet

# Crear el enrutador y registrar los ViewSets de Producto y Lote
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'ubicacion', UbicacionViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'tipo', TipoViewSet)


# Incluir las rutas registradas en urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('productolotes/', ObtenerProductoView.as_view(), name='productolotes'),
    path('ubicacionproductos/', ObtenerUbicacionView.as_view(), name='ubicacionproductos'),
    path('proveedorlotes/', ObtenerProveedorView.as_view(), name='proveedorlotes'),
    path('cantidadtotal/', ObtenerCantidadTotalPorProductoView.as_view(), name='cantidadtotal'),
    path('lotescaducar/', LotesProximosACaducarView.as_view(), name='lotescaducar'),
    path('lotereciente/', LoteMasRecienteView.as_view(), name='lotereciente'),
]
