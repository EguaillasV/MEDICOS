# pacuentes/forms.py
from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'cedula', 'dni', 'birth_date', 'gender', 
            'phone', 'email', 'address', 'blood_type', 'estado_civil', 'foto', 
            'antecedentes_personales', 'antecedentes_quirurgicos', 'antecedentes_familiares', 
            'alergias', 'medicamentos_actuales', 'habitos_toxicos', 'vacunas'
        ]
    
    # Si necesitas personalizar la validación de la foto, puedes agregarlo aquí
    foto = forms.ImageField(required=False)  # Foto no es obligatoria
