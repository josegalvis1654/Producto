from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.response import Response

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class Crear:
    def crear_producto(self, request):
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            id_tipo = request.POST.get('idtipo')
            id_ubicacion = request.POST.get('idubicacion')
            if nombre and id_tipo and id_ubicacion:  # Verificar que todos los datos existan
                producto = Producto(
                    nombre=nombre,
                    tipo_id=id_tipo,
                    ubicacion_id=id_ubicacion
                )
                producto.save()
