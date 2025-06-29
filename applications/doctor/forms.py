from django import forms
from .models import Doctor, Especialidad,Cargo
import datetime
from django.forms.widgets import ClearableFileInput, DateInput, TimeInput, TextInput
from django.forms.widgets import FileInput



class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'foto': FileInput(),  # no ClearableFileInput
            'fecha_nacimiento': DateInput(attrs={'type': 'date'}),
            'hora_inicio': TimeInput(attrs={'type': 'time'}),
            'hora_fin': TimeInput(attrs={'type': 'time'}),
            'nombres': forms.TextInput(attrs={
                'placeholder': 'Nombres completos',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'apellidos': forms.TextInput(attrs={
                'placeholder': 'Apellidos completos',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'ruc': forms.TextInput(attrs={
                'placeholder': 'Ej: 1723456789001',
                'maxlength': '13',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'fecha_nacimiento': DateInput(attrs={
                'type': 'date',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'hora_inicio': TimeInput(attrs={
                'type': 'time',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'hora_fin': TimeInput(attrs={
                'type': 'time',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Dirección exacta del consultorio',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'telefonos': forms.TextInput(attrs={
                'placeholder': 'Ej: 0991234567',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ejemplo@correo.com',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'latitud': forms.NumberInput(attrs={
                'step': '0.000001',
                'placeholder': '-0.180653',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'longitud': forms.NumberInput(attrs={
                'step': '0.000001',
                'placeholder': '-78.467838',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'codigo_unico_doctor': forms.TextInput(attrs={
                'placeholder': 'Código asignado por el sistema o colegio médico',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'duracion_atencion': forms.NumberInput(attrs={
                'step': '1',
                'min': '5',
                'max': '120',
                'placeholder': 'Ej: 30',
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'curriculum': ClearableFileInput(attrs={
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'firma_digital': ClearableFileInput(attrs={
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'imagen_receta': ClearableFileInput(attrs={
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'horario_atencion': TextInput(attrs={
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2',
                'placeholder': 'Ej: 08:00 - 16:00'
            }),
             'especialidad': forms.SelectMultiple(attrs={
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
                
            
        }
            
            
        
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




class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input w-full border border-gray-300 rounded-md px-4 py-2'
            }),
            'descripcion': forms.Textarea(attrs={
                'rows': 3,  
                'class': 'form-textarea w-full border border-gray-300 rounded-md px-4 py-2 resize-none'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-blue-600'
            }),
        }