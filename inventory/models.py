from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Categoria(models.Model):
    categoria= models.CharField(max_length=45)
    def __str__(self):
        return self.categoria

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Proveedor(models.Model):
    proveedor=models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    nombreEmpleado=models.CharField('Nombre del empleado',max_length=45)

    def __str__(self):
        return self.proveedor

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
class Producto(models.Model):
    codigo=models.CharField(max_length=45,null=True, blank=True)
    producto=models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    cantidad_total=models.IntegerField('Stock')
    precio_compra=models.FloatField('Precio de compra',max_length=45)
    precio_venta=models.FloatField('Precio de venta',max_length=20)
    categoria=models.ForeignKey(Categoria,null=False, on_delete=models.CASCADE)
    proveedor=models.ForeignKey(Proveedor,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.producto

    def toJSON(self):
        item = model_to_dict(self)
        item['precio_compra'] = format(self.precio_compra,'.2f')
        item['precio_venta'] = format(self.precio_venta,'.2f')   
        item['categoria'] = self.categoria.toJSON()
        return item