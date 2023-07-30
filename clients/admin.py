from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from clients.models import Cliente
# Register your models here.


class clienteAdmin(ImportExportModelAdmin):
    list_display=("nombre","identificacion","telefono1","telefono2","correo",)

admin.site.register(Cliente,clienteAdmin)
