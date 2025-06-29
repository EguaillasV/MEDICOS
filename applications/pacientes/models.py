from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

# Validación personalizada para la cédula ecuatoriana
def valida_cedula(value):
    ced = str(value)
    if not ced.isdigit() or len(ced) != 10:
        raise ValidationError("La cédula debe tener 10 dígitos numéricos.")
    provincia = int(ced[:2])
    if provincia < 1 or provincia > 24:
        raise ValidationError("Código de provincia inválido en la cédula.")
    tercer = int(ced[2])
    if tercer >= 6:
        raise ValidationError("El tercer dígito de la cédula es inválido.")
    coeficientes = [2,1,2,1,2,1,2,1,2]
    total = 0
    for i in range(9):
        d = int(ced[i]) * coeficientes[i]
        if d >= 10:
            d -= 9
        total += d
    next_ten = ((total + 9) // 10) * 10
    verificador = int(ced[9])
    if next_ten - total != verificador:
        raise ValidationError("Dígito verificador inválido en la cédula.")
   

# Modelo de Patient sin ForeignKey en el tipo de sangre
class Patient(models.Model):
    first_name = models.CharField("Nombres", max_length=150)
    last_name = models.CharField("Apellidos", max_length=150)
    cedula = models.CharField("Cédula ecuatoriana", max_length=10, validators=[valida_cedula], unique=True)
    dni = models.CharField("DNI internacional", max_length=30, blank=True, null=True,
        validators=[RegexValidator(r'^[A-Za-z0-9\-\. ]{5,30}$', "Debe ser pasaporte, DNI, CURP u otro válido.")]
    )
    birth_date = models.DateField("Fecha de nacimiento")
    gender = models.CharField("Sexo", max_length=1, choices=[('M','Masculino'),('F','Femenino'),('O','Otro')],)
    phone = models.CharField("Teléfono(s)", max_length=50, blank=True, null=True)
    email = models.EmailField("Correo electrónico", blank=True, null=True, unique=True)
    address = models.CharField("Dirección", max_length=255, blank=True, null=True)

    # Tipo de sangre (manteniéndolo como un CharField con choices)
    blood_type = models.CharField(
        "Tipo de sangre",
        max_length=3,
        blank=True, null=True,
        choices=[('A+','A+'), ('A-','A-'),
                 ('B+','B+'), ('B-','B-'),
                 ('AB+','AB+'), ('AB-','AB-'),
                 ('O+','O+'), ('O-','O-')]
    )

    # Información adicional
    estado_civil = models.CharField(
    max_length=12,
    choices=[('S','Soltero'), ('C','Casado'), ('D','Divorciado'), ('V','Viudo'), ('U','Unido')],
    verbose_name="Estado Civil",
     # Establecer valor por defecto 'Soltero'
    )
    latitud = models.DecimalField(max_digits=18, decimal_places=6, verbose_name="Latitud", null=True, blank=True)
    longitud = models.DecimalField(max_digits=18, decimal_places=6, verbose_name="Longitud", null=True, blank=True)
    foto = models.ImageField(upload_to='applications/pacientes/', null=True, blank=True, verbose_name="Foto")
    
    # Historia Clínica
    antecedentes_personales = models.TextField(blank=True, null=True, verbose_name="Antecedentes personales patológicos")
    antecedentes_quirurgicos = models.TextField(blank=True, null=True, verbose_name="Antecedentes quirúrgicos")
    antecedentes_familiares = models.TextField(blank=True, null=True, verbose_name="Antecedentes familiares")
    alergias = models.TextField(blank=True, null=True, verbose_name="Alergias")
    medicamentos_actuales = models.TextField(blank=True, null=True, verbose_name="Medicamentos actuales")
    habitos_toxicos = models.CharField(max_length=200, default='ninguno', verbose_name="Hábitos tóxicos o perjudiciales")
    vacunas = models.TextField(blank=True, null=True, verbose_name="Vacunas")
    antecedentes_gineco_obstetricos = models.TextField(blank=True, null=True, verbose_name="Antecedentes gineco-obstétricos")
    
    activo = models.BooleanField(default=True, verbose_name="Activo")

  
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.cedula})"

    # Propiedades
    @property
    def nombre_completo(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def edad(self):
        if not self.birth_date:
            return None
        today = date.today()
        edad = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            edad -= 1
        return edad

    @property
    def get_image(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        return '/static/img/usuario_anonimo.png'

    @staticmethod
    def cantidad_pacientes():
        return Patient.objects.count()
