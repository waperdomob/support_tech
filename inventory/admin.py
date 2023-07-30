from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from inventory.models import *
# Register your models here.


class categoriasAdmin(admin.ModelAdmin):
    list_display=("categoria",)
class productoAdmin(ImportExportModelAdmin):
    list_display=("codigo","producto","descripcion","cantidad_total","precio_compra","precio_venta","categoria",)

class proveedorAdmin(admin.ModelAdmin):
    list_display= ("proveedor","telefono","nombreEmpleado",)

admin.site.register(Producto,productoAdmin)
admin.site.register(Categoria,categoriasAdmin)
admin.site.register(Proveedor,proveedorAdmin)
