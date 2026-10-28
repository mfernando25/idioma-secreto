"""Ejemplo de transformación: si una pieza es Z, sustituirla por 0."""

ACTIVA = True
TIPO = "transformacion"
ORDEN = 20

PIEZA_ORIGEN = "z"
REEMPLAZO = "0"


def aplicar(piezas, palabra_original):
    """Cambia la pieza completa z por 0, sin alterar sílabas como 'zu'."""
    resultado = []
    for pieza in piezas:
        if pieza.casefold() == PIEZA_ORIGEN.casefold():
            resultado.append(REEMPLAZO)
        else:
            resultado.append(pieza)
    return resultado
