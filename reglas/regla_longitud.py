"""Ejemplo de validación: limitar la longitud de la palabra secreta."""

ACTIVA = True
TIPO = "validacion"
ORDEN = 20

MIN_CARACTERES = 1
# El alfabeto usa piezas de dos o tres caracteres y el prefijo añade dos.
# Este valor permite traducir muchas palabras habituales; ajústalo para tu idioma.
MAX_CARACTERES = 20


def validar(piezas, palabra_original):
    """Devuelve None si la longitud cumple el límite o explica el error."""
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
