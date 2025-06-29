from django.db import models
from django.core.exceptions import ValidationError

# Validación personalizada para el RUC
def valida_ruc(value):
    if len(value) != 13:
        raise ValidationError("El RUC debe tener 13 caracteres.")
    # Aquí puedes agregar más reglas de validación si es necesario

class Especialidad(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre de la Especialidad",
        help_text="Ejemplo: Cardiología, Pediatría, Ginecología"
    )
    
    descripcion = models.TextField(
        verbose_name="Descripción",
        null=True,
        blank=True,
        help_text="Breve explicación o enfoque de la especialidad (opcional)."
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Marcar como inactivo para ocultar esta especialidad en el sistema."
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = "Especialidad médica"
        verbose_name_plural = "Especialidades médicas"

    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombres = models.CharField(
        max_length=100,
        verbose_name="Nombres"
    )
    apellidos = models.CharField(
        max_length=100,
        verbose_name="Apellidos"
    )
    ruc = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="Ruc",
        validators=[valida_ruc],
        help_text="Ingrese un RUC válido (persona natural, sociedad o extranjero)."
    )
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de Nacimiento"
    )
    direccion = models.CharField(
        max_length=255,
        verbose_name="Dirección de Trabajo",
        help_text="Ubicación física donde atiende el doctor."
    )
    latitud = models.DecimalField(
        max_digits=18,
        decimal_places=6,
        verbose_name="Latitud",
        null=True,
        blank=True,
        help_text="Coordenada GPS (opcional)."
    )
    longitud = models.DecimalField(
        max_digits=18,
        decimal_places=6,
        verbose_name="Longitud",
        null=True,
        blank=True,
        help_text="Coordenada GPS (opcional)."
    )
    codigo_unico_doctor = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Código Único del Doctor",
        help_text="Identificador interno único para el doctor."
    )
    especialidad = models.ManyToManyField(
        'Especialidad',
        verbose_name="Especialidades",
        related_name="especialidades",
        help_text="Seleccione una o más especialidades médicas."
    )
    telefonos = models.CharField(
        max_length=20,
        verbose_name="Teléfonos",
        help_text="Número de contacto. Puede ser celular o fijo."
    )
    email = models.EmailField(
        verbose_name="Correo Electrónico",
        null=True,
        blank=True,
        help_text="Correo de contacto (opcional)."
    )
    horario_atencion = models.TextField(
        verbose_name="Horario de Atención",
        help_text="Ejemplo: Lunes a Viernes, 08h00 - 13h00"
    )
    duracion_atencion = models.PositiveIntegerField(
        verbose_name="Duración de Cita (minutos)",
        default=30,
        help_text="Tiempo estándar asignado a cada paciente."
    )
    curriculum = models.FileField(
        upload_to='applications/curriculums/',
        verbose_name="Currículum Vitae",
        null=True,
        blank=True,
        help_text="Archivo PDF o DOC (opcional)."
    )
    firma_digital = models.ImageField(
        upload_to='applications/firmas/',
        verbose_name="Firma Digital",
        null=True,
        blank=True,
        help_text="Imagen que será usada para firmar digitalmente."
    )
    foto = models.ImageField(
        upload_to='applications/doctor/',
        verbose_name="Foto",
        null=True,
        blank=True
    )
    
    
    imagen_receta = models.ImageField(
        upload_to='applications/recetas/',
        verbose_name="Imagen para Recetas",
        null=True,
        blank=True,
        help_text="Encabezado o firma que se mostrará en recetas médicas."
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Si está desmarcado, el doctor no podrá ser asignado a consultas."
    )

    @property
    def nombre_completo(self):
        return f"{self.apellidos} {self.nombres}"

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        ordering = ['apellidos', 'nombres']



class Cargo(models.Model):
    # Nombre del cargo (ej. Médico, Enfermero, Administrador, etc.)
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre del Cargo",
        help_text="Ej.: Médico, Enfermero, Administrador"
    )

    # Descripción del cargo (opcional)
    descripcion = models.TextField(
        verbose_name="Descripción del Cargo",
        null=True,
        blank=True,
        help_text="Descripción breve del rol que cumple este cargo (opcional)."
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Desactiva este cargo si ya no se usa en el sistema."
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['nombre']  # Orden alfabético en listados del admin