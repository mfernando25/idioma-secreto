"""Gestión del diccionario persistente en formato JSON."""

import json
from pathlib import Path


CARPETA_DATOS = Path(__file__).resolve().parent / "datos"
ARCHIVO_DICCIONARIO = CARPETA_DATOS / "diccionario.json"


def cargar_diccionario():
    """Lee el diccionario guardado en disco."""
    CARPETA_DATOS.mkdir(parents=True, exist_ok=True)
    if not ARCHIVO_DICCIONARIO.exists():
        return {}

    try:
        with ARCHIVO_DICCIONARIO.open("r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
    except json.JSONDecodeError as error:
        raise ValueError(
            "datos/diccionario.json contiene JSON inválido. "
            "No se sobrescribió para proteger los datos existentes."
        ) from error

    if not isinstance(contenido, dict):
        raise ValueError("El diccionario JSON debe contener un objeto.")
    return contenido


def guardar_diccionario(contenido):
    """Escribe el diccionario con formato legible y de forma segura."""
    CARPETA_DATOS.mkdir(parents=True, exist_ok=True)
    archivo_temporal = ARCHIVO_DICCIONARIO.with_suffix(".tmp")
    with archivo_temporal.open("w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, ensure_ascii=False, indent=4)
        archivo.write("\n")
    archivo_temporal.replace(ARCHIVO_DICCIONARIO)


def registrar_traduccion(original, traduccion):
    """Guarda o actualiza una traducción sin duplicar mayúsculas/minúsculas."""
    contenido = cargar_diccionario()
    contenido[original.casefold()] = {
        "original": original,
        "traduccion": traduccion,
    }
    guardar_diccionario(contenido)


def obtener_entradas():
    """Devuelve traducciones ordenadas por palabra original."""
    contenido = cargar_diccionario()
    entradas = list(contenido.values())
    entradas.sort(key=lambda entrada: entrada.get("original", "").casefold())
    return entradas
