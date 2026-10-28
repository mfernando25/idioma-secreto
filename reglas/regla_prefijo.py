"""Regla de transformación: añadir un prefijo."""

ACTIVA = True
TIPO = "transformacion"
ORDEN = 10

# Cambia esta pieza para definir el comienzo del idioma secreto.
PREFIJO = "pe"


def aplicar(piezas, palabra_original):
    """Devuelve las piezas con el prefijo al comienzo."""
    return [PREFIJO] + piezas
