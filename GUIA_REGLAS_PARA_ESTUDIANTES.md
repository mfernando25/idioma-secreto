# Guía de inspiración: reglas para el idioma secreto

Esta guía reúne ideas de las propuestas del aula y las agrupa cuando varias sugerencias describen una regla parecida. No es necesario activar o implementar todas. La idea es elegir una propuesta, diseñar su lógica, programarla y probar cómo interactúa con otras reglas.

**Sobre los conteos:** el número indica cuántos estudiantes propusieron esa regla o ideas cercanas, agrupadas por tema. Un mismo estudiante pudo sugerir más de una regla, por lo que los conteos de distintas filas se superponen.

## 1. Tres reglas de ejemplo ya implementadas

Estas reglas funcionan en el programa y permiten estudiar cómo se estructura un módulo.

| Regla propuesta | N.º de estudiantes | Posible uso |
|---|---:|---|
| Exigir un prefijo al comienzo | 5 | Hacer que la palabra secreta empiece con una pieza definida, como \`PE\`, \`war\`, \`bh\` o \`kx\`. |
| Reemplazar la pieza Z por 0 | 1 | Cambiar una pieza que sea exactamente \`z\` por el número \`0\`, sin modificar sílabas como \`zu\`. |
| Limitar la longitud de la traducción | 7 | Definir el mínimo y el máximo de caracteres que puede tener la palabra secreta. |

Están en \`reglas/\`. Se pueden modificar sus parámetros o desactivar con \`ACTIVA = False\`.

## 2. Tres plantillas incompletas para practicar

Las plantillas están en \`plantillas/\`. **No contienen la solución completa y no se ejecutan automáticamente.** Sirven como punto de partida para que el estudiante implemente la lógica.

| Regla propuesta | N.º de estudiantes | Posible uso |
|---|---:|---|
| Terminar la palabra secreta con un número | 10 (ideas cercanas sobre terminaciones) | Añadir un número al final para establecer una forma constante de las palabras. Plantilla: \`plantilla_terminar_numero.py\`. |
| Exigir que la palabra secreta contenga un número | 2 | Rechazar una traducción si no tiene ningún dígito. Plantilla: \`plantilla_contiene_numero.py\`. |
| Prohibir que una pieza se repita en la misma palabra | 4 | Evitar que una misma sílaba o pieza aparezca más de una vez. Plantilla: \`plantilla_no_repetir_piezas.py\`. |

Para usarlas:

1. Copia la plantilla elegida a la carpeta \`reglas/\`.
2. Cambia el nombre para que empiece por \`regla_\`, por ejemplo, \`regla_terminar_numero.py\`.
3. Completa las partes marcadas con \`RETO\`.
4. Cambia \`ACTIVA = False\` a \`ACTIVA = True\` cuando la regla esté implementada.
5. Ejecuta el programa y prueba un caso que cumpla la regla y otro que no.

## 3. Otras reglas propuestas para analizar y programar

Estas ideas se incluyen para inspirar el trabajo de los estudiantes. No se proporciona una plantilla con la solución: el grupo debe decidir cómo implementarlas dentro del esquema común.

| Regla propuesta | N.º de estudiantes | Posible uso |
|---|---:|---|
| Exigir al menos una vocal | 1 | Rechazar palabras secretas sin vocales. Considerar si otra regla ya garantiza una vocal. |
| Prohibir dos números consecutivos | 1 | Evitar secuencias como \`44\` o \`09\`. |
| Convertir un número en una pieza del idioma | 1 | Sustituir un dígito por una sílaba elegida en un pequeño diccionario. |
| Prohibir números o eliminarlos | 3 | Rechazar resultados que contienen dígitos o quitarlos durante la transformación. |
| Controlar repeticiones de caracteres | 7 | Limitar caracteres repetidos, reducir vocales duplicadas o evitar tres consonantes seguidas. |
| Sustituir letras, números o secuencias | 8 | Aplicar cambios definidos, por ejemplo, sustituir una letra o una combinación concreta por otra. |
| Exigir o prohibir una pieza o secuencia | 5 | Exigir que aparezca una secuencia o prohibir una combinación como \`gaa\`. |
| Limitar los caracteres permitidos | 5 | Aceptar solo letras, solo números o un tipo de combinación; permitir o eliminar símbolos. |
| Controlar mayúsculas y minúsculas | 6 | Convertir la salida a mayúsculas, cambiar el inicio o aplicar un formato definido. |
| Limitar el número o la proporción de vocales | 4 | Definir un máximo de vocales o exigir que sean un porcentaje de la palabra. |
| Terminar en una vocal | 3 | Exigir que la palabra secreta termine en una vocal. |
| Exigir vocales distintas | 1 | Rechazar palabras que repiten una vocal cuando se requiere variedad. |
| Evitar la misma vocal en piezas consecutivas | 1 | Comparar las vocales de piezas vecinas y evitar una repetición del patrón. |
| Exigir longitud par | 2 | Aceptar solo palabras secretas con un número par de caracteres. |
| Invertir palabras largas | 1 | Invertir el resultado cuando supera una longitud elegida. |
| Eliminar caracteres o secuencias concretas | 4 | Retirar un guion, un símbolo o una secuencia como \`uo\` o \`89\`. |
| Modificar una posición específica | 4 | Insertar, duplicar o reemplazar una pieza en una posición acordada, como la tercera. |
| Comparar la primera y la última pieza | 2 | Exigir que sean diferentes o que ambas comiencen con la misma letra. |
| Evitar coincidencias entre piezas vecinas | 1 | Impedir que el último carácter de una pieza coincida con el primero de la siguiente. |
| Exigir piezas de determinadas longitudes | 1 | Requerir, por ejemplo, una pieza de dos caracteres y otra de tres o más. |
| Controlar consonantes consecutivas | 1 | Rechazar palabras con tres consonantes seguidas. |
| Evitar entradas duplicadas en el diccionario | 2 | Evitar registros repetidos; el diccionario actualiza la entrada de una misma palabra ignorando diferencias de mayúsculas/minúsculas. |

## 4. Ideas para una etapa posterior

Estas propuestas trabajan sobre una frase completa o requieren comparar varias palabras. Es preferible abordarlas después de dominar las reglas de una sola palabra:

- Barajar o invertir cada palabra según su posición par dentro de una frase.
- Unir todas las palabras, eliminar los espacios e invertir la frase completa.
- Insertar una palabra adicional cada dos palabras de una frase.
- Crear palabras palíndromas con producciones simétricas o limitar globalmente la repetición de símbolos.

## 5. Cómo funciona la estructura de una regla

Los módulos se colocan dentro de \`reglas/\` y deben seguir una forma común:

- \`ACTIVA\`: \`True\` si se ejecuta, \`False\` si se ignora.
- \`TIPO\`: \`"transformacion"\` si modifica las piezas o \`"validacion"\` si comprueba una condición.
- \`ORDEN\`: opcional; si no se define, se usa el valor 50.
- Una transformación implementa \`aplicar(piezas, palabra_original)\` y devuelve una lista de piezas.
- Una validación implementa \`validar(piezas, palabra_original)\`. Devuelve \`None\` si la palabra cumple la regla o un mensaje de error si no la cumple.

Las transformaciones se aplican primero y las validaciones después. Dentro de cada fase, las reglas se ejecutan por orden numérico ascendente. Si una validación falla, esa palabra no se registra en el diccionario.

## 6. Desafío recomendado

Al elegir una regla, el estudiante debe:

1. Explicar la condición o transformación con sus propias palabras.
2. Identificar qué variable necesita leer o modificar.
3. Implementar la lógica sin alterar el menú ni el diccionario.
4. Probar al menos un ejemplo que cumpla y otro que falle.
5. Comprobar si otra regla activa cambia el resultado o hace que su regla pierda sentido.

Algunas reglas pueden entrar en conflicto. Por ejemplo, exigir números y prohibirlos a la vez, exigir exactamente tres piezas y una cantidad par, o prohibir repeticiones y exigir una pieza repetida. El grupo debe elegir las reglas que definan su idioma y justificar la combinación.
