from django.db import models

# Create your models here.
class Ubicacion(models.Model): 
    ubicacion= models. CharField(max_length=20)
    def __str__(self):
         return self.ubicacion

class Tipo (models.Model): 
    tipo=  models.CharField(max_length=20)
    def __str__(self):
         return self.tipo

class Estado (models.Model):
    estado= models.CharField(max_length=20)
    def __str__(self):
         return self.estado

class Producto (models.Model):
    nombre= models.CharField(max_length=20)
    tipo= models.ForeignKey(Tipo,on_delete=models.CASCADE)
    ubicacion= models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    def __str__(self):
         return self.nombre

class Lote (models. Model):
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    fechaentrega= models.DateField(null=True,blank=True)
    estado= models.ForeignKey(Estado,on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    fechacaducidad= models.DateField(null=True,blank=True)
    proveedor= models.CharField(max_length=20)
    def __str__(self):
        return self.producto