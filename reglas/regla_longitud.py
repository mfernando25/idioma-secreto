"""Regla de validación: limitar los caracteres del resultado secreto."""

ACTIVA = True
TIPO = "validacion"
ORDEN = 20

MIN_CARACTERES = 1
MAX_CARACTERES = 12


def validar(piezas, palabra_original):
    """Comprueba que el resultado respete los límites configurados."""
    palabra_secreta = "".join(piezas)
    longitud = len(palabra_secreta)

    if longitud < MIN_CARACTERES:
        return f"la traducción necesita al menos {MIN_CARACTERES} caracteres."
    if longitud > MAX_CARACTERES:
        return (
            f"la traducción tiene {longitud} caracteres; el máximo permitido "
            f"es {MAX_CARACTERES}."
        )
    return None
