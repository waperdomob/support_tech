from pickle import TRUE
from django.db import models
from datetime import datetime
from django.forms import model_to_dict

from inventory.models import  Producto
from clients.models import Cliente
from django.contrib.auth.models import User
# Create your models here.


class MetodoPagos(models.Model):
    metodoPago= models.CharField('Metodo de pago',max_length=45)
    def __str__(self):
        return self.metodoPago
    def toJSON(self):
        item = model_to_dict(self)

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    metodoPago = models.ForeignKey(MetodoPagos, on_delete=models.CASCADE)
    fecha_compra = models.DateField('Fecha de compra',default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    impuesto = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    descuento = models.DecimalField(default=0.00 , null=True, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cliente.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.toJSON()
        item['metodoPago'] = self.metodoPago.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['descuento'] = format(self.descuento, '.2f')
        item['total'] = format(self.total, '.2f')
        item['fecha_compra'] = self.fecha_compra.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.producto.producto

    def toJSON(self):
        item = model_to_dict(self, exclude=['venta'])
        item['producto'] = self.producto.toJSON()
        item['precio'] = format(self.precio, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']


class Cotizacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    impuesto = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    descuento = models.DecimalField(default=0.00 , null=True, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cliente.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['descuento'] = format(self.descuento, '.2f')
        item['total'] = format(self.total, '.2f')
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'
        ordering = ['id']


class DetCotizacion(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.producto.producto

    def toJSON(self):
        item = model_to_dict(self, exclude=['venta'])
        item['producto'] = self.producto.toJSON()
        item['precio'] = format(self.precio, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de cotizacion'
        verbose_name_plural = 'Detalle de cotizaciones'
        ordering = ['id']


