"""Regla de validación: impedir piezas iguales consecutivas."""


def validar(piezas):
    """Devuelve (True, mensaje) si no hay piezas consecutivas repetidas."""
    for posicion in range(1, len(piezas)):
        pieza_anterior = piezas[posicion - 1]
        pieza_actual = piezas[posicion]
        if pieza_anterior == pieza_actual:
            return False, f"la pieza '{pieza_actual}' aparece dos veces seguidas."
    return True, ""
