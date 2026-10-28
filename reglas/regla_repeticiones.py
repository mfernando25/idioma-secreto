"""Regla de validación: controlar piezas secretas repetidas."""

ACTIVA = False  # Desactivada inicialmente para permitir traducir palabras comunes.
TIPO = "validacion"
ORDEN = 10

# "todas": no se permite repetir ninguna pieza dentro de la palabra.
# "consecutivas": solo se prohíbe que dos piezas vecinas sean iguales.
MODO = "todas"


def validar(piezas, palabra_original):
    """Devuelve None si es válida o un mensaje si encuentra una repetición."""
    if MODO == "consecutivas":
        for posicion in range(1, len(piezas)):
            if piezas[posicion].casefold() == piezas[posicion - 1].casefold():
                return f"la pieza '{piezas[posicion]}' aparece dos veces seguidas."
        return None

    if MODO == "todas":
        piezas_vistas = set()
        for pieza in piezas:
            clave = pieza.casefold()
            if clave in piezas_vistas:
                return f"la pieza '{pieza}' aparece más de una vez."
            piezas_vistas.add(clave)
        return None

    return "MODO debe ser 'todas' o 'consecutivas'."
