from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Diagnosis


class DiagnosisListView(ListView):
    model = Diagnosis
    template_name = 'diagnosticos/list.html'
    context_object_name = 'diagnosticos'
    paginate_by = 4 

    def get_queryset(self):
        qs = super().get_queryset().select_related('patient')
        q = self.request.GET.get('q', '').strip()
        status = self.request.GET.get('status', '').strip().lower()

        if q:
            qs = qs.filter(
                Q(description__icontains=q) |
                Q(icd_code__icontains=q) |
                Q(patient__first_name__icontains=q) |
                Q(patient__last_name__icontains=q)
            )

        if status == 'activo':
            qs = qs.filter(is_active=True)
        elif status == 'inactivo':
            qs = qs.filter(is_active=False)

        return qs
class DiagnosisCreateView(CreateView):
    model = Diagnosis
    fields = ['patient', 'description', 'icd_code', 'notes', 'is_active']
    template_name = 'diagnosticos/form.html'
    success_url = reverse_lazy('diagnosticos:list')

class DiagnosisUpdateView(UpdateView):
    model = Diagnosis
    fields = ['patient', 'description', 'icd_code', 'notes', 'is_active']
    template_name = 'diagnosticos/form.html'
    success_url = reverse_lazy('diagnosticos:list')

class DiagnosisDeleteView(DeleteView):
    model = Diagnosis
    template_name = 'diagnosticos/confirm_delete.html'
    success_url = reverse_lazy('diagnosticos:list')

class MenuDiagnosticoView(TemplateView):
    template_name = "diagnosticos/form.html"

class DiagnosisDetailView(DetailView):
    model = Diagnosis
    template_name = 'diagnosticos/detail.html'
    context_object_name = 'diagnosis'