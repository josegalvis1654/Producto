from django.db import models

# Create your models here.
class Ubicacion(models.Model): 
    Ubicacion= models. CharField(max_length=20)

class Tipo (models.Model): 
    Tipo=  models.CharField(max_length=20)

class Estado (models.Model):
    Estado= models.CharField(max_length=20)

class Producto (models.Model):
    Nombre= models.CharField(max_length=20)
    IdTipo= models.ForeignKey(Tipo,on_delete=models.CASCADE)
    IdUbicacion= models.ForeignKey(Ubicacion,on_delete=models.CASCADE)

class Lote (models. Model):
    IdProducto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    FechaEntrega= models.DateField(null=True)
    IdEstado= models.ForeignKey(Estado,on_delete=models.CASCADE)
    Cantidad= models.IntegerField()
    FechaCaducidad= models.DateField(null=True)