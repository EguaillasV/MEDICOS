from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombres', 'apellidos', 'cedula_ecuatoriana', 'dni',
            'fecha_nacimiento', 'cargo', 'sueldo',
            'fecha_ingreso', 'direccion', 'latitud', 'longitud',
            'foto', 'activo'
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'latitud': forms.NumberInput(attrs={'step': 'any'}),
            'longitud': forms.NumberInput(attrs={'step': 'any'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cedula = cleaned_data.get('cedula_ecuatoriana')
        dni = cleaned_data.get('dni')
        
        if not cedula and not dni:
            raise forms.ValidationError("Debe proporcionar al menos una identificación: Cédula o DNI.")

        return cleaned_data
