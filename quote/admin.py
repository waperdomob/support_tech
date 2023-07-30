from django.contrib import admin

from quote import *
from sales.models import Cotizacion, DetCotizacion
# Register your models here.



class cotizacionAdmin(admin.ModelAdmin):
    list_display=("cliente","fecha","subtotal","impuesto","descuento","total",)

class detallecotizacionAdmin(admin.ModelAdmin):
    list_display=("cotizacion","producto","precio","cant","subtotal",)

admin.site.register(Cotizacion,cotizacionAdmin)
admin.site.register(DetCotizacion,detallecotizacionAdmin)

# Register your models here.
