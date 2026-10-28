# Guía de inspiración: reglas para el idioma secreto

Esta guía reúne ideas que surgieron en las propuestas del aula y las agrupa para evitar repetir reglas parecidas. Los ejemplos son opciones para inspirarse: **no hay que activar todas las reglas al mismo tiempo**.

El número indica cuántos estudiantes propusieron esa idea o una variante cercana. Como cada estudiante entregó varias ideas, los conteos de distintas filas se superponen.

## 1. Cinco reglas iniciales de la versión 2

| Regla propuesta | N.º de estudiantes | Posible uso |
|---|---:|---|
| Evitar piezas repetidas dentro de una palabra | 4 | Impedir que una misma pieza o sílaba aparezca más de una vez, o limitar la regla solo a piezas consecutivas. |
| Limitar la longitud de la traducción | 7 | Definir un mínimo y un máximo de caracteres permitidos en la palabra secreta. |
| Exigir al menos una vocal | 1 | Rechazar palabras secretas que no contengan ninguna vocal. |
| Reemplazar Z por 0 | 1 | Cambiar la letra `Z` por el número `0` en las piezas resultantes. |
| Exigir un prefijo | 5 | Hacer que la palabra secreta comience con una pieza definida, por ejemplo `PE`, `war`, `bh`, `kx` o, bajo una condición, `uo`. |

Estas cinco reglas ya tienen módulos en la versión 2. La regla de repetición está desactivada inicialmente porque puede rechazar palabras corrientes; se puede activar en `reglas/regla_repeticiones.py`. Los parámetros y la activación de cada regla están dentro de su propio archivo.

## 2. Otras reglas sencillas que se pueden agregar

Las siguientes propuestas también encajan en el esquema del proyecto: procesar las piezas de una palabra, transformarlas y validar el resultado. Algunas reglas se solapan porque pueden ser variantes de la misma idea.

| Regla propuesta | N.º de estudiantes | Posible uso |
|---|---:|---|
| Añadir o exigir una terminación | 10 | Agregar una pieza al final o exigir que la palabra termine en una secuencia, vocal, número o signo de puntuación. |
| Controlar la cantidad de piezas o sílabas | 4 | Establecer el mínimo, máximo o número exacto de piezas; por ejemplo, exigir exactamente tres. |
| Exigir que la palabra contenga un número | 2 | Rechazar una traducción si no aparece al menos un dígito. |
| Prohibir o eliminar números | 3 | Hacer que las palabras secretas no contengan dígitos o quitarlos durante la transformación. |
| Prohibir dos números consecutivos | 1 | Rechazar resultados que contengan secuencias como `44` o `09`. |
| Convertir un número en una pieza del idioma | 1 | Sustituir un dígito por una sílaba definida en un pequeño diccionario. |
| Controlar caracteres repetidos | 7 | Limitar repeticiones o comprimirlas; por ejemplo, reducir vocales duplicadas o evitar tres consonantes seguidas. |
| Sustituir letras, números o secuencias | 8 | Aplicar cambios definidos, como `g` por `2o1a`, `Z` por `0` o una secuencia concreta por otra. |
| Exigir o prohibir una pieza o secuencia | 5 | Exigir que aparezca una secuencia, prohibir `gaa` o rechazar una palabra que contenga una combinación elegida. |
| Limitar los caracteres permitidos | 5 | Aceptar solo letras, solo números o una combinación elegida; también se puede permitir o eliminar símbolos. |
| Controlar mayúsculas y minúsculas | 6 | Convertir toda la salida a mayúsculas, capitalizar el comienzo o aplicar un formato de letras repetidas. |
| Limitar la cantidad o proporción de vocales | 4 | Definir un máximo de vocales o exigir que representen un porcentaje de la palabra. |
| Terminar en una vocal | 3 | Exigir que la palabra secreta termine en una vocal o en una vocal abierta. |
| Exigir vocales distintas | 1 | Rechazar palabras que repitan una vocal cuando se exige variedad. |
| Evitar la misma vocal en piezas consecutivas | 1 | Comprobar la vocal de piezas vecinas y rechazar una repetición del patrón. |
| Exigir longitud par | 2 | Aceptar solo palabras secretas con un número par de caracteres. |
| Invertir palabras largas | 1 | Invertir la traducción cuando supere una longitud definida, por ejemplo seis caracteres. |
| Eliminar caracteres o secuencias concretas | 4 | Retirar un guion, un símbolo o una secuencia como `uo` o `89`. |
| Modificar una posición específica | 4 | Insertar, duplicar o reemplazar una pieza en una posición acordada, como la tercera. |
| Comparar la primera y la última pieza | 2 | Exigir que sean diferentes o que ambas comiencen con la misma letra. |
| Evitar choques entre piezas vecinas | 1 | Impedir que el último carácter de una pieza sea igual al primero de la siguiente. |
| Exigir piezas de determinadas longitudes | 1 | Requerir, por ejemplo, una pieza de dos caracteres y otra de tres o más. |
| Limitar consonantes consecutivas | 1 | Rechazar palabras que tengan tres consonantes seguidas. |
| Evitar entradas duplicadas en el diccionario | 2 | Impedir registros repetidos; actualmente, el diccionario ya actualiza la entrada de una misma palabra original en vez de crear otra por mayúsculas/minúsculas. |

## 3. Ideas que conviene dejar para otra etapa

Estas propuestas no son imposibles, pero no las recomiendo como primeras reglas porque trabajan con una frase completa, dependen de la posición de varias palabras o requieren diseñar un sistema de generación gramatical:

- Barajar o invertir cada palabra según su posición par en una frase.
- Unir todas las palabras de una frase, eliminar todos los espacios y luego invertir el texto completo.
- Insertar una palabra cada dos palabras de la frase.
- Crear palabras palíndromas mediante producciones simétricas o controlar globalmente las repeticiones de símbolos de una gramática.

Para empezar, conviene que cada regla afecte a **una palabra traducida**. Más adelante se puede diseñar un segundo tipo de regla que opere sobre frases completas.

## 4. Cómo incorporar una nueva regla en la versión 2

1. Crea un archivo dentro de `reglas/` cuyo nombre empiece por `regla_`, por ejemplo `regla_sufijo.py`.
2. Define en ese mismo archivo `ACTIVA`, `TIPO` y `ORDEN`, además de sus parámetros.
3. Si transforma la palabra, implementa `aplicar(piezas, palabra_original)` y devuelve la nueva lista de piezas.
4. Si comprueba una condición, implementa `validar(piezas, palabra_original)`: devuelve `None` si es válida o un mensaje de error si debe rechazarse.
5. Guarda el archivo y reinicia `python main.py`. El traductor detecta automáticamente el nuevo módulo; no hace falta modificar `traductor.py`, `main.py` ni `diccionario.py`.

### Plantilla de transformación

```python
# REGLA: describe aquí lo que hace.

ACTIVA = True
TIPO = "transformacion"
ORDEN = 40

# Parámetros propios de esta regla.
SUFIJO = "yu"


def aplicar(piezas, palabra_original):
    # Devuelve una nueva lista de piezas.
    return piezas + [SUFIJO]
```

### Plantilla de validación

```python
# REGLA: describe aquí la condición que comprueba.

ACTIVA = True
TIPO = "validacion"
ORDEN = 40


def validar(piezas, palabra_original):
    # Añade aquí la condición que quieras comprobar.
    # Ejemplo:
    # if "x" not in "".join(piezas):
    #     return "La palabra debe contener x."
    return None
```

La plantilla inicial no rechaza ninguna palabra. Descomenta y adapta el ejemplo cuando tengas clara la condición que quieres validar.

## 5. ¿Cómo funciona el orden?

- El traductor ejecuta primero todas las reglas con `TIPO = "transformacion"`, ordenadas por `ORDEN` de menor a mayor.
- Después ejecuta las reglas con `TIPO = "validacion"`, también de menor a mayor.
- Si una validación devuelve un mensaje de error, la palabra se rechaza y no se guarda.
- Puedes usar números como `10`, `20`, `30` y dejar intervalos para insertar reglas entre ellas. El orden solo organiza las reglas de una misma fase: las transformaciones siempre preceden a las validaciones.

**Importante:** algunas reglas se contradicen si se activan juntas. Por ejemplo, exigir un número y prohibir números, exigir exactamente tres piezas y exigir una cantidad par, o prohibir repeticiones y exigir piezas repetidas. El estudiante debe decidir qué reglas forman parte de su idioma y probar el conjunto completo.
