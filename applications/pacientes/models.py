from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

def valida_cedula(value):
    """
    Valida cédula ecuatoriana de 10 dígitos según el algoritmo del Módulo 10.
    """
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

class Patient(models.Model):
    first_name = models.CharField("Nombres", max_length=150)
    last_name  = models.CharField("Apellidos", max_length=150)
    cedula     = models.CharField(
        "Cédula ecuatoriana",
        max_length=10,
        validators=[valida_cedula],
        help_text="10 dígitos sin espacios ni guiones."
    )
    dni = models.CharField(
        "DNI internacional",
        max_length=30,
        blank=True, null=True,
        validators=[RegexValidator(
            regex=r'^[A-Za-z0-9\-\. ]{5,30}$',
            message="Debe ser pasaporte, DNI, CURP u otro válido."
        )],
        help_text="Opcional: pasaporte, DNI, CURP, etc."
    )
    birth_date = models.DateField("Fecha de nacimiento")
    gender = models.CharField(
        "Sexo",
        max_length=1,
        choices=[('M','Masculino'),('F','Femenino'),('O','Otro')],
        default='M'
    )
    phone = models.CharField(
        "Teléfono(s)",
        max_length=50,
        blank=True, null=True,
        help_text="Puede separar varios con comas."
    )
    email = models.EmailField(
        "Correo electrónico",
        blank=True, null=True,
        unique=True
    )
    address = models.CharField(
        "Dirección",
        max_length=255,
        blank=True, null=True
    )
    blood_type = models.CharField(
        "Tipo de sangre",
        max_length=3,
        blank=True, null=True,
        choices=[
            ('A+','A+'), ('A-','A-'),
            ('B+','B+'), ('B-','B-'),
            ('AB+','AB+'), ('AB-','AB-'),
            ('O+','O+'), ('O-','O-'),
        ]
    )
    created_at = models.DateTimeField("Creado el", auto_now_add=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.cedula})"
