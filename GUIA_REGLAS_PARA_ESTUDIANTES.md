# Guía de inspiración: reglas para el idioma secreto

Esta guía reúne ideas que surgieron de las propuestas del aula. Algunas se agrupan porque varios estudiantes sugirieron variantes de la misma regla. El objetivo es elegir una idea, diseñar su lógica, programarla y probar cómo interactúa con otras reglas.

**Sobre los conteos:** el número indica cuántos estudiantes propusieron esa regla o una idea cercana. Un mismo estudiante pudo sugerir varias reglas, por lo que los conteos de distintas filas se superponen.

> **Cómo ver las tablas:** abre esta guía en la vista normal de GitHub o en la vista previa de Markdown de VS Code. Las tablas se han definido como tablas HTML con encabezados explícitos, no como filas de texto separadas por barras verticales.

## 1. Tres reglas de ejemplo ya implementadas

Estas reglas funcionan en el programa y permiten estudiar cómo se estructura un módulo.

<table>
  <thead>
    <tr>
      <th scope="col">Regla propuesta</th>
      <th scope="col">N.º de estudiantes</th>
      <th scope="col">Posible uso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Exigir un prefijo al comienzo</td>
      <td>5</td>
      <td>Hacer que la palabra secreta empiece con una pieza definida, como <code>PE</code>, <code>war</code>, <code>bh</code> o <code>kx</code>.</td>
    </tr>
    <tr>
      <td>Reemplazar la pieza Z por 0</td>
      <td>1</td>
      <td>Cambiar una pieza que sea exactamente <code>z</code> por <code>0</code>, sin modificar sílabas como <code>zu</code>.</td>
    </tr>
    <tr>
      <td>Limitar la longitud de la traducción</td>
      <td>7</td>
      <td>Definir el mínimo y máximo de caracteres que puede tener la palabra secreta.</td>
    </tr>
  </tbody>
</table>

Los archivos están en <code>reglas/</code>. Puedes modificar sus parámetros o desactivarlos poniendo <code>ACTIVA = False</code>.

## 2. Tres plantillas incompletas para practicar

Las plantillas están en <code>plantillas/</code>. No contienen la solución completa ni se ejecutan automáticamente: el estudiante debe copiar una, completar la lógica y probarla.

<table>
  <thead>
    <tr>
      <th scope="col">Regla propuesta</th>
      <th scope="col">N.º de estudiantes</th>
      <th scope="col">Posible uso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Terminar la palabra secreta con un número</td>
      <td>10 (ideas cercanas sobre terminaciones)</td>
      <td>Añadir un número al final. Plantilla: <code>plantilla_terminar_numero.py</code>.</td>
    </tr>
    <tr>
      <td>Exigir que la palabra secreta contenga un número</td>
      <td>2</td>
      <td>Rechazar una traducción si no contiene ningún dígito. Plantilla: <code>plantilla_contiene_numero.py</code>.</td>
    </tr>
    <tr>
      <td>Prohibir que una pieza se repita en la misma palabra</td>
      <td>4</td>
      <td>Evitar que una misma sílaba o pieza aparezca más de una vez. Plantilla: <code>plantilla_no_repetir_piezas.py</code>.</td>
    </tr>
  </tbody>
</table>

Para usar una plantilla:

1. Cópiala a la carpeta <code>reglas/</code>.
2. Cambia el nombre para que empiece por <code>regla_</code>, por ejemplo, <code>regla_terminar_numero.py</code>.
3. Completa las partes marcadas con <code>RETO</code>.
4. Cambia <code>ACTIVA = False</code> a <code>ACTIVA = True</code> cuando esté implementada.
5. Prueba al menos un caso que cumple la regla y otro que no.

## 3. Otras reglas para analizar y programar

Estas propuestas sirven como inspiración. No se proporciona una plantilla con la solución: el grupo debe decidir cómo implementarlas usando la estructura común de reglas.

### 3.1 Números, longitud y repeticiones

<table>
  <thead>
    <tr>
      <th scope="col">Regla propuesta</th>
      <th scope="col">N.º de estudiantes</th>
      <th scope="col">Posible uso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Prohibir dos números consecutivos</td>
      <td>1</td>
      <td>Evitar secuencias como <code>44</code> o <code>09</code>.</td>
    </tr>
    <tr>
      <td>Convertir un número en una pieza del idioma</td>
      <td>1</td>
      <td>Sustituir un dígito por una sílaba elegida en un pequeño diccionario.</td>
    </tr>
    <tr>
      <td>Prohibir números o eliminarlos</td>
      <td>3</td>
      <td>Rechazar resultados con dígitos o quitarlos durante la transformación.</td>
    </tr>
    <tr>
      <td>Controlar repeticiones de caracteres</td>
      <td>7</td>
      <td>Reducir vocales duplicadas, limitar repeticiones o evitar tres consonantes seguidas.</td>
    </tr>
    <tr>
      <td>Limitar el número o la proporción de vocales</td>
      <td>4</td>
      <td>Definir un máximo de vocales o exigir que sean un porcentaje de la palabra.</td>
    </tr>
    <tr>
      <td>Exigir longitud par</td>
      <td>2</td>
      <td>Aceptar solo palabras secretas con un número par de caracteres.</td>
    </tr>
  </tbody>
</table>

### 3.2 Sustituciones y caracteres permitidos

<table>
  <thead>
    <tr>
      <th scope="col">Regla propuesta</th>
      <th scope="col">N.º de estudiantes</th>
      <th scope="col">Posible uso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sustituir letras, números o secuencias</td>
      <td>8</td>
      <td>Aplicar cambios definidos, por ejemplo, sustituir una letra o combinación por otra.</td>
    </tr>
    <tr>
      <td>Exigir o prohibir una pieza o secuencia</td>
      <td>5</td>
      <td>Exigir que aparezca una secuencia o prohibir una combinación como <code>gaa</code>.</td>
    </tr>
    <tr>
      <td>Limitar los caracteres permitidos</td>
      <td>5</td>
      <td>Aceptar solo letras, solo números o una combinación determinada; permitir o eliminar símbolos.</td>
    </tr>
    <tr>
      <td>Controlar mayúsculas y minúsculas</td>
      <td>6</td>
      <td>Convertir toda la salida a mayúsculas, cambiar el inicio o aplicar un formato definido.</td>
    </tr>
    <tr>
      <td>Eliminar caracteres o secuencias concretas</td>
      <td>4</td>
      <td>Retirar un guion, un símbolo o una secuencia como <code>uo</code> o <code>89</code>.</td>
    </tr>
  </tbody>
</table>

### 3.3 Vocales y estructura de las piezas

<table>
  <thead>
    <tr>
      <th scope="col">Regla propuesta</th>
      <th scope="col">N.º de estudiantes</th>
      <th scope="col">Posible uso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Exigir al menos una vocal</td>
      <td>1</td>
      <td>Rechazar palabras secretas sin vocales; comprobar primero si otra regla ya garantiza una vocal.</td>
    </tr>
    <tr>
      <td>Terminar en una vocal</td>
      <td>3</td>
      <td>Exigir que el último carácter de la palabra secreta sea una vocal.</td>
    </tr>
    <tr>
      <td>Exigir vocales distintas</td>
      <td>1</td>
      <td>Rechazar palabras que repitan una vocal cuando se requiere variedad.</td>
    </tr>
    <tr>
      <td>Evitar la misma vocal en piezas consecutivas</td>
      <td>1</td>
      <td>Comparar las vocales de piezas vecinas y evitar una repetición del patrón.</td>
    </tr>
    <tr>
      <td>Exigir piezas de determinadas longitudes</td>
      <td>1</td>
      <td>Requerir, por ejemplo, una pieza de dos caracteres y otra de tres o más.</td>
    </tr>
    <tr>
      <td>Controlar consonantes consecutivas</td>
      <td>1</td>
      <td>Rechazar palabras con tres consonantes seguidas.</td>
    </tr>
  </tbody>
</table>

### 3.4 Posiciones y organización de la palabra

<table>
  <thead>
    <tr>
      <th scope="col">Regla propuesta</th>
      <th scope="col">N.º de estudiantes</th>
      <th scope="col">Posible uso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Invertir palabras largas</td>
      <td>1</td>
      <td>Invertir el resultado cuando supera una longitud elegida.</td>
    </tr>
    <tr>
      <td>Modificar una posición específica</td>
      <td>4</td>
      <td>Insertar, duplicar o reemplazar una pieza en una posición acordada, como la tercera.</td>
    </tr>
    <tr>
      <td>Comparar la primera y la última pieza</td>
      <td>2</td>
      <td>Exigir que sean diferentes o que ambas comiencen con la misma letra.</td>
    </tr>
    <tr>
      <td>Evitar coincidencias entre piezas vecinas</td>
      <td>1</td>
      <td>Impedir que el último carácter de una pieza coincida con el primero de la siguiente.</td>
    </tr>
    <tr>
      <td>Evitar entradas duplicadas en el diccionario</td>
      <td>2</td>
      <td>Evitar registros repetidos; el diccionario ya actualiza la entrada de una palabra aunque cambien las mayúsculas.</td>
    </tr>
  </tbody>
</table>

## 4. Ideas para una etapa posterior

Estas propuestas trabajan sobre una frase completa o requieren comparar varias palabras. Es preferible abordarlas después de dominar las reglas de una sola palabra:

- Barajar o invertir cada palabra según su posición par dentro de una frase.
- Unir todas las palabras, eliminar los espacios e invertir la frase completa.
- Insertar una palabra adicional cada dos palabras de una frase.
- Crear palabras palíndromas con producciones simétricas o limitar globalmente la repetición de símbolos.

## 5. Cómo funciona la estructura de una regla

Cada archivo dentro de <code>reglas/</code> declara:

- <code>ACTIVA</code>: <code>True</code> si se ejecuta, <code>False</code> si se ignora.
- <code>TIPO</code>: <code>"transformacion"</code> si modifica las piezas o <code>"validacion"</code> si comprueba una condición.
- <code>ORDEN</code>: opcional; si no se define, se usa el valor 50.
- Una transformación implementa <code>aplicar(piezas, palabra_original)</code> y devuelve una lista de piezas.
- Una validación implementa <code>validar(piezas, palabra_original)</code>. Devuelve <code>None</code> si la palabra cumple la regla o un mensaje de error si no la cumple.

Las transformaciones se ejecutan primero y las validaciones después. Dentro de cada fase, las reglas se ejecutan por orden numérico ascendente. Si una validación falla, esa palabra no se registra en el diccionario.

## 6. Desafío recomendado

Al elegir una regla, el estudiante debe:

1. Explicar la condición o transformación con sus propias palabras.
2. Identificar qué variable necesita leer o modificar.
3. Implementar la lógica sin alterar el menú ni el diccionario.
4. Probar al menos un ejemplo que cumpla y otro que falle.
5. Comprobar si otra regla activa cambia el resultado o hace que su regla pierda sentido.

Algunas reglas pueden entrar en conflicto. Por ejemplo, exigir números y prohibirlos a la vez, exigir exactamente tres piezas y una cantidad par, o prohibir repeticiones y exigir una pieza repetida. El grupo debe elegir las reglas que definan su idioma y justificar la combinación.
