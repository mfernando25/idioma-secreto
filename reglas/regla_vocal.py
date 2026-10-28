"""Regla de validación: exigir al menos una vocal en la palabra secreta."""

ACTIVA = True
TIPO = "validacion"
ORDEN = 30

VOCALES = "aeiouáéíóúü"


def validar(piezas, palabra_original):
    """Comprueba si el resultado contiene al menos una vocal."""
    palabra_secreta = "".join(piezas).casefold()
    if not any(vocal in palabra_secreta for vocal in VOCALES):
        return "la palabra secreta debe contener al menos una vocal."
    return None
