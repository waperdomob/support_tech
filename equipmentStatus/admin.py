from django.contrib import admin

from equipmentStatus.models import *
# Register your models here.

class ingresoAdmin(admin.ModelAdmin):
    list_display=("cliente","fecha_ingreso",)

class equipoAdmin(admin.ModelAdmin):
    list_display=("equipo","estado","diagnostico","reporte_ingreso")

admin.site.register(Ingreso,ingresoAdmin)
admin.site.register(Equipo,equipoAdmin)



