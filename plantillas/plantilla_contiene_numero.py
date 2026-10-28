"""PLANTILLA 2: exigir que la palabra secreta contenga un número.

Copia este archivo a reglas/regla_contiene_numero.py.
Completa la validación antes de cambiar ACTIVA a True.
"""

ACTIVA = False
TIPO = "validacion"
# ORDEN = 50  # Opcional. Si lo omites, se utiliza el orden 50.


def validar(piezas, palabra_original):
    palabra_secreta = "".join(piezas)
    contiene_numero = False

    for caracter in palabra_secreta:
        # RETO: comprueba si el carácter es un dígito.
        # Si lo es, actualiza contiene_numero.
        pass

    # RETO: si no hay ningún dígito, devuelve un mensaje de error.
    # Si hay uno o más, devuelve None.
    raise NotImplementedError("Completa la regla que exige un número.")
