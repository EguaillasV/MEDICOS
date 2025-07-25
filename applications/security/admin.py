from django.contrib import admin
# security/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Menu, Module, GroupModulePermission
from django.apps import AppConfig


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'dni', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('dni', 'image', 'direction', 'phone')}),
    )

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order')
    search_fields = ('name',)
    ordering = ('order', 'name')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'menu', 'is_active', 'order')
    list_filter = ('menu', 'is_active')
    search_fields = ('name', 'url', 'description')
    ordering = ('menu', 'order', 'name')

@admin.register(GroupModulePermission)
class GroupModulePermissionAdmin(admin.ModelAdmin):
    list_display = ('group', 'module')
    list_filter = ('group', 'module')
    filter_horizontal = ('permissions',)

from applications.pacientes.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dni', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'dni')
    list_filter = ('gender', 'blood_type')

    
class DiagnosticosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.diagnosticos'

