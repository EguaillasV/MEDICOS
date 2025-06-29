from django import forms
from .models import Doctor, Especialidad
import datetime

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    # Campo de Especialidades con Widget de Selección Múltiple
    especialidades = forms.ModelMultipleChoiceField(
        queryset=Especialidad.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    # Lógica de validación adicional para el RUC
    def clean_ruc(self):
        ruc = self.cleaned_data['ruc']
        if not ruc.isdigit():
            raise forms.ValidationError("El RUC debe contener solo números.")
        return ruc

    # Validación para la fecha de nacimiento
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if fecha_nacimiento > datetime.date.today():
            raise forms.ValidationError("La fecha de nacimiento no puede ser futura.")
        return fecha_nacimiento

    # Validación para el teléfono
    def clean_telefonos(self):
        telefonos = self.cleaned_data['telefonos']
        if not telefonos.isdigit() or len(telefonos) < 7:
            raise forms.ValidationError("El número de teléfono debe ser válido.")
        return telefonos

    # Validación de la dirección
    def clean_direccion(self):
        direccion = self.cleaned_data['direccion']
        if not direccion:
            raise forms.ValidationError("La dirección de trabajo no puede estar vacía.")
        return direccion

    # Validación opcional para las coordenadas GPS
    def clean_latitud(self):
        latitud = self.cleaned_data.get('latitud')
        if latitud and (latitud < -90 or latitud > 90):
            raise forms.ValidationError("La latitud debe estar entre -90 y 90 grados.")
        return latitud

    def clean_longitud(self):
        longitud = self.cleaned_data.get('longitud')
        if longitud and (longitud < -180 or longitud > 180):
            raise forms.ValidationError("La longitud debe estar entre -180 y 180 grados.")
        return longitud
