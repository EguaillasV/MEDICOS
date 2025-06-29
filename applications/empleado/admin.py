from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cedula_ecuatoriana', 'cargo', 'activo')
    search_fields = ('nombres', 'apellidos', 'cedula_ecuatoriana')
    list_filter = ('cargo', 'activo')
