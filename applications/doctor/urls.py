from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.DoctorListView.as_view(), name='list'),  # Lista de doctores
    path('crear/', views.DoctorCreateView.as_view(), name='create'),  # Crear nuevo doctor
    path('<int:pk>/editar/', views.DoctorUpdateView.as_view(), name='update'),  # Editar doctor
    path('<int:pk>/', views.DoctorDetailView.as_view(), name='detail'),  # Ver detalle del doctor
    path('<int:pk>/eliminar/', views.DoctorDeleteView.as_view(), name='delete'),  # Eliminar doctor
]

