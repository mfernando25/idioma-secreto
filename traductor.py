"""Convierte palabras y frases utilizando el alfabeto y las reglas activas."""

import re

import configuracion
from alfabeto import ALFABETO, normalizar_letra
from reglas import regla_longitud, regla_prefijo, regla_repeticiones


def convertir_a_piezas(palabra):
    """Convierte las letras originales en piezas del idioma secreto."""
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
    """Devuelve (traducción, error); no escribe en el diccionario."""
    palabra = palabra.strip()
    if not palabra:
        return None, "la palabra no puede estar vacía."

    piezas, error = convertir_a_piezas(palabra)
    if error:
        return None, error

    # 1. Ejecutar las reglas que transforman las piezas.
    if configuracion.ACTIVAR_PREFIJO:
        piezas = regla_prefijo.aplicar(piezas, configuracion.PREFIJO)

    # 2. Comprobar las reglas de validación sobre el resultado final.
    if configuracion.ACTIVAR_SIN_REPETICIONES_CONSECUTIVAS:
        es_valida, mensaje = regla_repeticiones.validar(piezas)
        if not es_valida:
            return None, mensaje

    if configuracion.ACTIVAR_LONGITUD_MAXIMA:
        es_valida, mensaje = regla_longitud.validar(
            palabra,
            piezas,
            configuracion.MAX_CARACTERES_POR_LETRA,
        )
        if not es_valida:
            return None, mensaje

    return "".join(piezas), None


def traducir_frase(frase):
    """Traduce una frase sin guardarla; conserva espacios y puntuación.

    Las palabras que no superan las reglas se mantienen en el texto original.
    Devuelve (frase_traducida, lista_de_errores).
    """
    errores = []
    patron_palabras = r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+"

    def reemplazar_palabra(coincidencia):
        palabra = coincidencia.group(0)
        resultado, error = traducir_palabra(palabra)
        if error:
            errores.append((palabra, error))
            return palabra
        return resultado

    return re.sub(patron_palabras, reemplazar_palabra, frase), errores
