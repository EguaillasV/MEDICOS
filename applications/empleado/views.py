from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from applications.empleado.models import Empleado
from applications.empleado.forms import EmpleadoForm
from applications.security.components.mixin_crud import (
    ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
)


class EmpleadoListView(PermissionMixin, ListViewMixin, ListView):
    model = Empleado
    template_name = 'empleado/empleado_list.html'
    context_object_name = 'empleados'
    permission_required = 'view_empleado'


class EmpleadoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado:list')
    permission_required = 'add_empleado'

    def form_valid(self, form):
        messages.success(self.request, "Empleado registrado correctamente.")
        return super().form_valid(form)


class EmpleadoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado:list')
    permission_required = 'change_empleado'

    def form_valid(self, form):
        messages.success(self.request, "Empleado actualizado correctamente.")
        return super().form_valid(form)


class EmpleadoDetailView(PermissionMixin, DetailView):
    model = Empleado
    template_name = 'empleado/empleado_detail.html'
    context_object_name = 'empleado'
    permission_required = 'view_empleado'


class EmpleadoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Empleado
    template_name = 'empleado/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado:list')
    permission_required = 'delete_empleado'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Empleado eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
