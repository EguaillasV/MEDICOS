from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Patient
from django.shortcuts import render, get_object_or_404

class PatientListView(ListView):
    model = Patient
    template_name = 'pacientes/list.html'
    context_object_name = 'pacientes'
    def get_queryset(self):
        return Patient.objects.all()  

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'pacientes/form.html'
    fields = '__all__'
    success_url = reverse_lazy('pacientes:list')

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'pacientes/form.html'
    fields = '__all__'
    
    # Redirigir al detalle del paciente después de guardar los cambios
    def get_success_url(self):
        # Redirige a la página de detalles del paciente recién actualizado
        return reverse_lazy('pacientes:detail', kwargs={'pk': self.object.pk})

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'pacientes/confirm_delete.html'
    success_url = reverse_lazy('pacientes:list')

def patient_detail(request, pk):
    paciente = get_object_or_404(Patient, pk=pk)
    return render(request, 'pacientes/detail.html', {'paciente': paciente})
