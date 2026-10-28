# Creador de idioma secreto — versión 2

Programa didáctico en Python que traduce palabras y frases a través de un alfabeto editable y un conjunto de reglas modulares detectadas automáticamente. Solo utiliza la biblioteca estándar de Python; no necesita instalar paquetes adicionales.

## Ejecutar el programa

Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```bash
python main.py
```

En algunos equipos Windows también puedes usar `py main.py`.

## Menú

1. **Traducir una palabra:** traduce y guarda la pareja original/traducción en el diccionario local.
2. **Traducir una frase:** aplica el mismo proceso a cada palabra, conserva espacios y puntuación y muestra el resultado sin guardar la frase.
3. **Mostrar diccionario:** consulta las traducciones guardadas durante ejecuciones anteriores en ese equipo.
4. **Salir.**

## Archivos principales

- `main.py`: menú principal.
- `alfabeto.py`: equivalencias editables entre letras y piezas secretas.
- `traductor.py`: traduce las palabras, detecta los módulos de reglas y los ejecuta.
- `diccionario.py`: carga y guarda las traducciones en JSON.
- `reglas/`: cada archivo `regla_*.py` contiene una regla, sus parámetros, si está activa y su orden.
- `GUIA_REGLAS_PARA_ESTUDIANTES.md`: ideas de reglas agrupadas a partir de las propuestas del aula, con conteos y ejemplos de uso.
- `datos/diccionario.json`: se crea localmente y conserva las traducciones.

## Reglas incluidas

- `reglas/regla_prefijo.py`: añade el prefijo configurado. Está activa al inicio.
- `reglas/regla_reemplazar_z.py`: reemplaza `Z` o `z` por `0` dentro de las piezas. Está activa al inicio.
- `reglas/regla_repeticiones.py`: evita repetir piezas en cualquier posición o solo consecutivamente, según `MODO`. Está desactivada inicialmente para no rechazar palabras comunes.
- `reglas/regla_longitud.py`: limita la longitud de la palabra secreta, con mínimo y máximo configurables. El máximo inicial es 12 caracteres.
- `reglas/regla_vocal.py`: exige al menos una vocal en la palabra secreta.

## Cómo agregar una regla

1. Crea un archivo dentro de `reglas/`; su nombre debe comenzar con `regla_`, por ejemplo `regla_sufijo.py`.
2. Define `ACTIVA = True` o `False`, `TIPO = "transformacion"` o `"validacion"` y un `ORDEN` entero.
3. Para una transformación, crea `aplicar(piezas, palabra_original)`, que debe devolver una lista de piezas.
4. Para una validación, crea `validar(piezas, palabra_original)`, que debe devolver `None` si la palabra es válida o un mensaje de error si no lo es.
5. Guarda el archivo y reinicia el programa. El traductor detectará la nueva regla automáticamente.

Las transformaciones se ejecutan primero, en orden numérico. Después se ejecutan las validaciones, también en orden numérico. Una validación que devuelva un mensaje de error hace que la palabra sea rechazada y no se registre.

Consulta `GUIA_REGLAS_PARA_ESTUDIANTES.md` para plantillas y más ideas.

## Persistencia

Las traducciones se guardan en `datos/diccionario.json` y permanecen disponibles al cerrar y volver a ejecutar el programa en el mismo equipo. Ese archivo se excluye de Git para que los datos locales no se suban al repositorio.
