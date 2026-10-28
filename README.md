# Creador de idioma secreto — versión 1

Programa didáctico en Python que convierte palabras y frases mediante un alfabeto editable y aplica reglas independientes. Solo utiliza la biblioteca estándar de Python; no necesita instalar paquetes adicionales.

## Ejecutar el programa

1. Descarga el repositorio o clónalo con Git.
2. Abre una terminal dentro de la carpeta del proyecto.
3. Ejecuta `python main.py` (en algunos equipos Windows, `py main.py`).

## Menú

1. **Traducir una palabra:** traduce y guarda el par original/traducción en el diccionario local.
2. **Traducir una frase:** aplica el mismo proceso a cada palabra, conserva espacios y puntuación y muestra el resultado sin guardar la frase.
3. **Mostrar diccionario:** consulta las traducciones guardadas durante ejecuciones anteriores en ese equipo.
4. **Salir.**

## Archivos principales

- `main.py`: menú principal.
- `alfabeto.py`: equivalencias que pueden editar los estudiantes.
- `configuracion.py`: activación y parámetros de las reglas.
- `traductor.py`: proceso compartido para traducir palabras y frases.
- `diccionario.py`: carga y guardado de registros JSON.
- `reglas/regla_prefijo.py`: transformación que añade un prefijo.
- `reglas/regla_repeticiones.py`: valida que no haya piezas repetidas consecutivamente.
- `reglas/regla_longitud.py`: valida el máximo de caracteres con relación al original.
- `datos/diccionario.json`: se crea localmente para guardar las traducciones.

## Reglas incluidas

En `configuracion.py` se pueden activar, desactivar y parametrizar las reglas:

- **Prefijo:** añade `pe` al inicio. Cambia `PREFIJO` o desactiva `ACTIVAR_PREFIJO`.
- **Sin piezas repetidas consecutivamente:** rechaza una traducción si dos piezas vecinas son iguales.
- **Longitud máxima:** la traducción puede tener como máximo `MAX_CARACTERES_POR_LETRA` caracteres por cada carácter original.

Primero se aplican las transformaciones y después las validaciones. Si una validación falla, la palabra no se registra. En una frase, la palabra que falla se conserva en su forma original y el motivo se muestra al usuario.

## Cómo añadir una regla

1. Crea un archivo nuevo dentro de `reglas/`, por ejemplo `regla_sufijo.py`.
2. Escribe una función pequeña que reciba las variables necesarias y devuelva el resultado o el estado de validación.
3. Importa el módulo en `traductor.py` y llama la función en el punto adecuado del proceso.
4. Si la regla necesita parámetros, añade variables descriptivas en `configuracion.py`.

## Persistencia

Las traducciones registradas permanecen en `datos/diccionario.json` al cerrar y volver a ejecutar el programa **en el mismo equipo**. Ese archivo se excluye de Git para evitar subir datos generados localmente; cada usuario creará su propio diccionario a partir de `datos/diccionario.json.example`. Las modificaciones del alfabeto y de la configuración sí se guardan en Git cuando se confirman y publican los cambios.
