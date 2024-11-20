from rest_framework import viewsets
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
from django.db.models import Count,Sum,F
from rest_framework.response import Response
from rest_framework import status
from .models import Producto, Lote, Ubicacion, Estado, Tipo
from .serializers import ProductoSerializer, LoteSerializer, UbicacionSerializer, TipoSerializer, EstadoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()  # Define el conjunto de datos de productos
    serializer_class = ProductoSerializer  # Define el serializador a usar

    # Sobreescribiendo el método create para agregar una respuesta personalizada
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 'Producto creado exitosamente', 'producto': serializer.data}, status=status.HTTP_201_CREATED)

    # Sobreescribiendo el método update para agregar una respuesta personalizada
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Para soportar actualizaciones parciales
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'status': 'Producto actualizado exitosamente', 'producto': serializer.data})

    # Sobreescribiendo el método destroy para agregar una respuesta personalizada
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'Producto eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()  # Obtiene todos los registros de Lote
    serializer_class = LoteSerializer  # Serializador para Lote

    # Sobreescribimos el método create para personalizar la respuesta al crear un lote
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 'Lote creado exitosamente', 'lote': serializer.data}, status=status.HTTP_201_CREATED)

    # Sobreescribimos el método update para personalizar la respuesta al actualizar un lote
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Soporta actualizaciones parciales
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'status': 'Lote actualizado exitosamente', 'lote': serializer.data})

    # Sobreescribimos el método destroy para personalizar la respuesta al eliminar un lote
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'Lote eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()  # Define el conjunto de datos de productos
    serializer_class = UbicacionSerializer  # Define el serializador a usar

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()  # Define el conjunto de datos de productos
    serializer_class = TipoSerializer  # Define el serializador a usar

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()  # Define el conjunto de datos de productos
    serializer_class = EstadoSerializer  # Define el serializador a usar

class ObtenerProductoView(View):
    def get(self, request):
        # Agrupa por 'producto', cuenta los lotes y ordena en orden descendente
        resultado = Lote.objects.values('producto__nombre').annotate(total_lotes=Count('producto')).order_by('-total_lotes')
        # Obtener el producto con el mayor número de lotes
        if resultado:
            producto_mas_lotes = resultado[0]
            return JsonResponse({'producto_mas_lotes': producto_mas_lotes}, safe=False)
        return JsonResponse({'message': 'No hay datos disponibles'}, status=404)

class ObtenerUbicacionView(View):
    def get(self, request):
        # Agrupa por 'ubicacion', cuenta los productos y ordena en orden descendente
        resultado = Producto.objects.values('ubicacion__ubicacion').annotate(total_productos=Count('ubicacion')).order_by('-total_productos')
        # Obtener la ubicación con el mayor número de productos
        if resultado:
            ubicacion_mas_productos = resultado[0]
            return JsonResponse({'ubicacion_mas_productos': ubicacion_mas_productos}, safe=False)
        return JsonResponse({'message': 'No hay datos disponibles'}, status=404)

class ObtenerProveedorView(View):
    def get(self, request):
        # Agrupa por 'proveedor', cuenta los lotes y ordena en orden descendente
        resultado = Lote.objects.values('proveedor').annotate(total_lotes=Count('proveedor')).order_by('-total_lotes')
        # Obtener el proveedor con el mayor número de lotes
        if resultado:
            proveedor_mas_lotes = resultado[0]
            return JsonResponse({'proveedor_mas_lotes': proveedor_mas_lotes}, safe=False)
        return JsonResponse({'message': 'No hay datos disponibles'}, status=404)

class ObtenerCantidadTotalPorProductoView(View):
    def get(self, request):
        # Agrupa por 'producto' y suma las cantidades de cada grupo
        resultado = Lote.objects.values('producto__nombre').annotate(total_cantidad=Sum('cantidad')).order_by('-total_cantidad')
        if resultado:
            return JsonResponse(list(resultado), safe=False)
        return JsonResponse({'message': 'No hay datos disponibles'}, status=404)
    
class LotesProximosACaducarView(View):
    def get(self, request):
        # Obtener la fecha actual
        fecha_actual = timezone.now().date()
        # Filtrar los lotes cuya fecha de caducidad es mayor o igual a hoy, y ordenar por fecha de caducidad ascendente
        resultado = (Lote.objects.filter(fechacaducidad__gte=fecha_actual).order_by('fechacaducidad')[:10])       
        # Convertir el resultado a una lista de diccionarios para enviarlo en formato JSON
        lotes = list(resultado.values(
            'id', 
            'producto__nombre',  
            'fechaentrega', 
            'estado',     
            'cantidad', 
            'fechacaducidad', 
            'proveedor'
        ))
        if lotes:
            return JsonResponse(lotes, safe=False)
        return JsonResponse({'message': 'No hay lotes proximos a caducar'}, status=404)

class LoteMasRecienteView(View):
    def get(self, request):
        # Obtener el lote más reciente basado en la fecha de entrega
        lote_mas_reciente = Lote.objects.order_by('-fechaentrega').values('producto__nombre','fechaentrega').first()
        if lote_mas_reciente:
            return JsonResponse(lote_mas_reciente)
        # Si no hay lotes, se envía un mensaje
        return JsonResponse({'message': 'No se encontraron lotes'}, status=404)