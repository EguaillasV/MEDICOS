from django.contrib import admin
from .models import Doctor, Especialidad

# Registrar el modelo Doctor
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'ruc', 'fecha_nacimiento', 'direccion', 'activo')
    search_fields = ('nombres', 'apellidos', 'ruc', 'email')
    list_filter = ('activo', 'especialidad')

admin.site.register(Doctor, DoctorAdmin)

# Registrar el modelo Especialidad si aún no está registrado
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'activo')
    search_fields = ('nombre',)

admin.site.register(Especialidad, EspecialidadAdmin)


