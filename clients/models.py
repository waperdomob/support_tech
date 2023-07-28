from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.conf import settings

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    identificacion=models.CharField(max_length=20, null=True, blank=True)
    direccion=models.CharField(max_length=100, null=True, blank=True)
    telefono1=models.CharField(max_length=100, null=True, blank=True)
    telefono2=models.CharField(max_length=100, null=True, blank=True)    
    correo=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre
        
    def toJSON(self):
        item = model_to_dict(self)
        return item
