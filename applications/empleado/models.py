from django.db import models
from django.core.validators import RegexValidator
from applications.utils.validations import valida_cedula  
from applications.doctor.models import Cargo  

class Empleado(models.Model):
    nombres = models.CharField(
        max_length=100,
        verbose_name="Nombre del Empleado"
    )
    apellidos = models.CharField(
        max_length=100,
        verbose_name="Apellido del Empleado"
    )
    cedula_ecuatoriana = models.CharField(
        max_length=10,
        verbose_name="Cédula",
        validators=[valida_cedula],
        help_text="Ingrese el número de cédula sin espacios ni guiones."
    )
    dni = models.CharField(
        max_length=30,
        verbose_name="DNI Internacional",
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9\-\. ]{5,30}$',
                message="Ingrese un documento válido (letras, números, guiones o puntos)."
            )
        ],
        help_text="Pasaporte, DNI, CURP u otro documento válido internacionalmente."
    )
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de Nacimiento"
    )
    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.PROTECT,
        verbose_name="Cargo",
        related_name="empleados"
    )
    sueldo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Sueldo"
    )
    fecha_ingreso = models.DateField(
        verbose_name="Fecha de Ingreso"
    )
    direccion = models.CharField(
        max_length=255,
        verbose_name="Dirección"
    )
    latitud = models.FloatField(
        verbose_name="Latitud",
        null=True,
        blank=True
    )
    longitud = models.FloatField(
        verbose_name="Longitud",
        null=True,
        blank=True
    )
    foto = models.ImageField(
        upload_to='core/empleados/',
        verbose_name="Foto del Empleado",
        null=True,
        blank=True
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    @property
    def nombre_completo(self):
        return f"{self.apellidos} {self.nombres}"

    def __str__(self):
        return self.nombre_completo

    class Meta:
        ordering = ['apellidos', 'nombres']
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
