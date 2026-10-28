"""Regla de transformación sugerida por una estudiante: sustituir Z por 0."""

ACTIVA = True
TIPO = "transformacion"
ORDEN = 20

LETRA_ORIGEN = "z"
REEMPLAZO = "0"


def aplicar(piezas, palabra_original):
    """Reemplaza la letra configurada dentro de cada pieza traducida."""
    origen = LETRA_ORIGEN
    return [
        pieza.replace(origen.lower(), REEMPLAZO).replace(origen.upper(), REEMPLAZO)
        for pieza in piezas
    ]
