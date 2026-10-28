"""Regla de validación: limitar la longitud de la traducción."""


def validar(palabra_original, piezas, maximo_por_letra):
    """Comprueba que la traducción no supere el límite configurado."""
    palabra_secreta = "".join(piezas)
    longitud_maxima = len(palabra_original) * maximo_por_letra
    if len(palabra_secreta) > longitud_maxima:
        return (
            False,
            f"la traducción tiene {len(palabra_secreta)} caracteres y "
            f"el máximo permitido es {longitud_maxima}.",
        )
    return True, ""
