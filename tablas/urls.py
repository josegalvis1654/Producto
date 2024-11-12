from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, LoteViewSet, ObtenerProductoView,ObtenerUbicacionView,ObtenerProveedorView,ObtenerCantidadTotalPorProductoView,LotesProximosACaducarView,LoteMasRecienteView

# Crear el enrutador y registrar los ViewSets de Producto y Lote
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'lotes', LoteViewSet)

# Incluir las rutas registradas en urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('productolotes/', ObtenerProductoView.as_view(), name='productolotes'),
    path('ubicacionproductos/', ObtenerUbicacionView.as_view(), name='ubicacionproductos'),
    path('proveedorlotes/', ObtenerProveedorView.as_view(), name='proveedorlotes'),
    path('cantidad-total/', ObtenerCantidadTotalPorProductoView.as_view(), name='cantidad_total'),
    path('lotescaducar/', LotesProximosACaducarView.as_view(), name='lotescaducar'),
    path('lotereciente/', LoteMasRecienteView.as_view(), name='lotereciente'),
]
