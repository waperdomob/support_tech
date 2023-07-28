from django.db import models
from datetime import datetime
from django.forms import model_to_dict

# Create your models here.
from clients.models import Cliente

class Ingreso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField('Fecha de ingreso',default=datetime.now)
    
    def __str__(self):
        return self.cliente.nombre

class Equipo(models.Model):
    equipo= models.CharField(max_length=45)
    estado = models.CharField(max_length=45)
    diagnostico = models.TextField()
    reporte_ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)

    def __str__(self):
        return self.equipo

    def toJSON(self):
        item = model_to_dict(self)
        return item