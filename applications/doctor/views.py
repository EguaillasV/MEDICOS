from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Doctor
from django.views.generic import ListView
from .forms import DoctorForm

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Doctor
from .forms import DoctorForm

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor/doctor_form.html'
    success_url = reverse_lazy('doctor:list')  # Aquí es donde debes redirigir al listado de doctores

    def form_valid(self, form):
        # Guardar el doctor
        response = super().form_valid(form)

        # Aquí aseguramos que las especialidades seleccionadas se guarden correctamente
        especialidades = form.cleaned_data.get('especialidades')
        if especialidades:
            self.object.especialidad.set(especialidades)  # Asocia las especialidades al doctor guardado

        return response


# Vista para editar los datos de un Doctor
class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor/doctor_form.html'  # La plantilla que usas para editar
    success_url = reverse_lazy('doctor:detail')  # Redirige a la página de detalle del doctor después de guardar

# Vista para ver los detalles de un Doctor
class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor/doctor_detail.html'  # La plantilla para ver detalles del doctor
    context_object_name = 'doctor'

# Vista para eliminar un Doctor
class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor/confirm_delete.html'  # La plantilla de confirmación de eliminación
    success_url = reverse_lazy('doctor:list')  # Redirige a la lista de doctores después de eliminar


class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor/doctor_list.html'  # Asegúrate de tener una plantilla para esta vista
    context_object_name = 'doctores'  # Nombre del contexto que pasas a la plantilla

    def get_queryset(self):
        return Doctor.objects.all()  # Aquí puedes aplicar filtros si es necesario