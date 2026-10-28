"""Regla de transformación: añadir una pieza al inicio."""


def aplicar(piezas, prefijo):
    """Devuelve una nueva lista con el prefijo delante de las piezas."""
    return [prefijo] + piezas
