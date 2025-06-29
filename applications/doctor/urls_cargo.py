# applications/doctor/urls_cargo.py
from django.urls import path
from .views import (
    CargoListView, CargoCreateView, CargoUpdateView,
    CargoDetailView, CargoDeleteView
)

app_name = "cargo"

urlpatterns = [
    path('', CargoListView.as_view(), name='list'),
    path('nuevo/', CargoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', CargoUpdateView.as_view(), name='update'),
    path('<int:pk>/detalle/', CargoDetailView.as_view(), name='detail'),
    path('<int:pk>/eliminar/', CargoDeleteView.as_view(), name='delete'),
]
