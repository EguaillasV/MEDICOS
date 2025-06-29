from django.urls import path
from .views import (
    EmpleadoListView,
    EmpleadoCreateView,
    EmpleadoUpdateView,
    EmpleadoDetailView,
    EmpleadoDeleteView,
)

app_name = 'empleado'

urlpatterns = [
    path('', EmpleadoListView.as_view(), name='list'),
    path('nuevo/', EmpleadoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='update'),
    path('<int:pk>/detalle/', EmpleadoDetailView.as_view(), name='detail'),
    path('<int:pk>/eliminar/', EmpleadoDeleteView.as_view(), name='delete'),
]
