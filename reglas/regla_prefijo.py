"""Ejemplo de transformación basada en la propuesta de comenzar con PE."""

ACTIVA = True
TIPO = "transformacion"
ORDEN = 10

# Cambia el prefijo si tu grupo ha elegido otro.
PREFIJO = "PE"


def aplicar(piezas, palabra_original):
    """Devuelve las piezas con el prefijo al comienzo."""
    return [PREFIJO] + piezas
