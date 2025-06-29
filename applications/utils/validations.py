from django.core.exceptions import ValidationError

def valida_cedula(value):
    """
    Valida que la cédula ecuatoriana tenga 10 dígitos numéricos y sea válida.
    """
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("La cédula debe contener exactamente 10 dígitos numéricos.")
    
    provincia = int(value[:2])
    if provincia < 1 or provincia > 24:
        raise ValidationError("La cédula no corresponde a una provincia válida.")

    coeficientes = [2,1,2,1,2,1,2,1,2]
    suma = 0

    for i in range(9):
        val = int(value[i]) * coeficientes[i]
        if val >= 10:
            val -= 9
        suma += val

    verificador = int(value[9])
    if (suma % 10 == 0 and verificador != 0) or (10 - (suma % 10) != verificador):
        raise ValidationError("La cédula ingresada no es válida.")
