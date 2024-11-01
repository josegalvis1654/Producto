from django.db import models

# Create your models here.
class Ubicacion(models.Model): 
    ubicacion= models. CharField(max_length=20)

class Tipo (models.Model): 
    tipo=  models.CharField(max_length=20)

class Estado (models.Model):
    estado= models.CharField(max_length=20)

class Producto (models.Model):
    nombre= models.CharField(max_length=20)
    tipo= models.ForeignKey(Tipo,on_delete=models.CASCADE)
    ubicacion= models.ForeignKey(Ubicacion,on_delete=models.CASCADE)

class Lote (models. Model):
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    fechaentrega= models.DateField(null=True,blank=True)
    estado= models.ForeignKey(Estado,on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    fechacaducidad= models.DateField(null=True,blank=True)