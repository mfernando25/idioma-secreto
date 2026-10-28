"""Traducción común y detección automática de reglas.

Para añadir una regla nueva, basta con crear reglas/regla_nombre.py siguiendo
el formato documentado en GUIA_REGLAS_PARA_ESTUDIANTES.md. No hay que editar
este archivo cada vez que se añade una regla.
"""

import importlib
import pkgutil

import reglas
from alfabeto import ALFABETO, normalizar_letra

TIPOS_DE_REGLA = ("transformacion", "validacion")


def descubrir_reglas():
    """Encuentra los archivos regla_*.py y los ordena por fase y ORDEN."""
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
                f"{informacion.name}.py necesita una variable ACTIVA = True o False."
            )

        tipo = getattr(modulo, "TIPO", None)
        if tipo not in TIPOS_DE_REGLA:
            raise ValueError(
                f"{informacion.name}.py debe tener TIPO = 'transformacion' "
                "o TIPO = 'validacion'."
            )

        orden = getattr(modulo, "ORDEN", None)
        if not isinstance(orden, int):
            raise ValueError(f"{informacion.name}.py necesita un ORDEN entero.")

        funcion = "aplicar" if tipo == "transformacion" else "validar"
        if not callable(getattr(modulo, funcion, None)):
            raise ValueError(
                f"{informacion.name}.py necesita la función {funcion}()."
            )

        # Todas las transformaciones se ejecutan antes que las validaciones.
        fase = 0 if tipo == "transformacion" else 1
        modulos.append((fase, orden, informacion.name, modulo))

    modulos.sort(key=lambda elemento: (elemento[0], elemento[1], elemento[2]))
    return [elemento[3] for elemento in modulos]


def convertir_a_piezas(palabra):
    """Convierte cada letra original en una pieza de nuestro alfabeto."""
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
    """Devuelve (traducción, error) sin guardar la palabra en el diccionario."""
    palabra = palabra.strip()
    if not palabra:
        return None, "la palabra no puede estar vacía."

    piezas, error = convertir_a_piezas(palabra)
    if error:
        return None, error

    try:
        modulos = descubrir_reglas()
        for modulo in modulos:
            if not modulo.ACTIVA:
                continue

            nombre_regla = modulo.__name__.split(".")[-1]
            if modulo.TIPO == "transformacion":
                # Una transformación recibe una lista de piezas y devuelve
                # otra lista. Le pasamos una copia para evitar cambios ocultos.
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
                # Una validación devuelve None si la palabra es válida o un
                # mensaje de texto si debe rechazarse.
                mensaje = modulo.validar(list(piezas), palabra)
                if mensaje:
                    return None, f"{nombre_regla}: {mensaje}"

    except Exception as error_regla:
        return None, f"Error en una regla: {error_regla}"

    return "".join(piezas), None


def traducir_frase(frase):
    """Traduce cada palabra y conserva espacios y signos de puntuación.

    Si una palabra no supera una validación, se conserva en el texto original
    y se devuelve su motivo en una lista de errores. La frase no se guarda.
    """
    import re

    errores = []
    patron_palabras = r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+"

    def reemplazar_palabra(coincidencia):
        palabra_original = coincidencia.group(0)
        traduccion, error = traducir_palabra(palabra_original)
        if error:
            errores.append((palabra_original, error))
            return palabra_original
        return traduccion

    return re.sub(patron_palabras, reemplazar_palabra, frase), errores
