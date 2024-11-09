from rest_framework import viewsets
from django.db.models import Count,Sum
from rest_framework.response import Response
from rest_framework import status
from .models import Producto, Lote
from .serializers import ProductoSerializer, LoteSerializer


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

class Informe(viewsets.ViewSet):
    def obtener_producto_con_mas_lotes():
        # Agrupa por 'producto', cuenta los lotes y ordena en orden descendente
        resultado = Lote.objects.values('producto').annotate(total_lotes=Count('producto')).order_by('-total_lotes')
        # Obtener el producto con el mayor número de lotes
        if resultado:
            producto_mas_lotes = resultado[0]
            return producto_mas_lotes
        return None
    def obtener_ubicacion_con_mas_productos():
        # Agrupa por 'ubicacion', cuenta los productos y ordena en orden descendente
        resultado = Producto.objects.values('ubicacion').annotate(total_productos=Count('ubicacion')).order_by('-total_productos')
        # Obtener la ubicación con el mayor número de productos
        if resultado:
            ubicacion_mas_productos = resultado[0]
            return ubicacion_mas_productos
        return None
    def obtener_proveedor_con_mas_lotes():
        # Agrupa por 'proveedor', cuenta los lotes y ordena en orden descendente
        resultado = Lote.objects.values('proveedor').annotate(total_lotes=Count('proveedor')).order_by('-total_lotes')
        # Obtener el proveedor con el mayor número de lotes
        if resultado:
            proveedor_mas_lotes = resultado[0]
            return proveedor_mas_lotes
        return None
    def obtener_total_cantidad_por_producto():
        # Agrupa por 'producto' y suma las cantidades de cada grupo
        resultado = Lote.objects.values('producto').annotate(total_cantidad=Sum('cantidad')).order_by('-total_cantidad')      
        return resultado