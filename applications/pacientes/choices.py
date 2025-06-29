# applications/pacientes/choices.py

from django.db import models

class SexoChoices(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'
    OTRO = 'O', 'Otro'

class EstadoCivilChoices(models.TextChoices):
    SOLTERO = 'S', 'Soltero'
    CASADO = 'C', 'Casado'
    DIVORCIADO = 'D', 'Divorciado'
    VIUDO = 'V', 'Viudo'
    UNIDO = 'U', 'Unido'
