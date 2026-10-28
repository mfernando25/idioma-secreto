"""Traducción y detección automática de reglas didácticas.

Para añadir una regla, crea un archivo regla_*.py dentro de reglas/.
No necesitas editar este archivo ni el menú.
"""

import importlib
import pkgutil

import reglas
from alfabeto import ALFABETO, normalizar_letra

TIPOS_DE_REGLA = ("transformacion", "validacion")
ORDEN_PREDETERMINADO = 50


def descubrir_reglas():
    """Encuentra reglas y las ordena por fase y orden."""
    modulos = []

    for informacion in pkgutil.iter_modules(reglas.__path__):
        if not informacion.name.startswith("regla_"):
            continue

        nombre_completo = f"reglas.{informacion.name}"
        try:
            modulo = importlib.import_module(nombre_completo)
        except Exception as error:
            raise ValueError(
                f"No se pudo cargar {informacion.name}.py: {error}"
            ) from error

        if not hasattr(modulo, "ACTIVA") or not isinstance(modulo.ACTIVA, bool):
            raise ValueError(
                f"{informacion.name}.py necesita ACTIVA = True o False."
            )

        tipo = getattr(modulo, "TIPO", None)
        if tipo not in TIPOS_DE_REGLA:
            raise ValueError(
                f"{informacion.name}.py necesita TIPO = "
                "'transformacion' o 'validacion'."
            )

        # ORDEN es opcional. Si no se indica, usamos 50.
        orden = getattr(modulo, "ORDEN", ORDEN_PREDETERMINADO)
        if not isinstance(orden, int):
            raise ValueError(
                f"En {informacion.name}.py, ORDEN debe ser un número entero."
            )

        funcion = "aplicar" if tipo == "transformacion" else "validar"
        if not callable(getattr(modulo, funcion, None)):
            raise ValueError(
                f"{informacion.name}.py necesita la función {funcion}()."
            )

        # Las transformaciones siempre van antes que las validaciones.
        fase = 0 if tipo == "transformacion" else 1
        modulos.append((fase, orden, informacion.name, modulo))

    modulos.sort(key=lambda elemento: (elemento[0], elemento[1], elemento[2]))
    return [elemento[3] for elemento in modulos]


def convertir_a_piezas(palabra):
    """Convierte las letras originales en las piezas de nuestro alfabeto."""
    piezas = []

    for letra in palabra:
        if not letra.isalpha():
            return None, (
                "escribe una sola palabra usando letras, sin espacios, "
                "números ni signos de puntuación."
            )

        letra_normalizada = normalizar_letra(letra)
        if letra_normalizada not in ALFABETO:
            return None, f"no hay una equivalencia definida para '{letra}'."

        piezas.append(ALFABETO[letra_normalizada])

    return piezas, None


def traducir_palabra(palabra):
    """Devuelve (traducción, error); no guarda datos en el diccionario."""
    palabra = palabra.strip()
    if not palabra:
        return None, "la palabra no puede estar vacía."

    piezas, error = convertir_a_piezas(palabra)
    if error:
        return None, error

    try:
        for modulo in descubrir_reglas():
            if not modulo.ACTIVA:
                continue

            nombre_regla = modulo.__name__.split(".")[-1]

            if modulo.TIPO == "transformacion":
                # Las transformaciones reciben y devuelven listas de piezas.
                nuevas_piezas = modulo.aplicar(list(piezas), palabra)
                if not isinstance(nuevas_piezas, list) or not all(
                    isinstance(pieza, str) for pieza in nuevas_piezas
                ):
                    return None, (
                        f"{nombre_regla}: aplicar() debe devolver una lista "
                        "de piezas de texto."
                    )
                piezas = nuevas_piezas
            else:
                # Las validaciones devuelven None o un mensaje de error.
                mensaje = modulo.validar(list(piezas), palabra)
                if mensaje is not None:
                    if not isinstance(mensaje, str):
                        return None, (
                            f"{nombre_regla}: validar() debe devolver None "
                            "o un mensaje de texto."
                        )
                    if mensaje:
                        return None, f"{nombre_regla}: {mensaje}"

    except Exception as error_regla:
        return None, f"Error en una regla: {error_regla}"

    return "".join(piezas), None


def traducir_frase(frase):
    """Traduce cada palabra; conserva espacios y signos de puntuación."""
    import re

    errores = []
    patron_palabras = r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+"

    def reemplazar_palabra(coincidencia):
        original = coincidencia.group(0)
        traduccion, error = traducir_palabra(original)
        if error:
            errores.append((original, error))
            return original
        return traduccion

    return re.sub(patron_palabras, reemplazar_palabra, frase), errores
