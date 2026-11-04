# Creador de idioma secreto — versión 3

Programa didáctico en Python para traducir palabras y frases mediante un alfabeto editable y reglas modulares. No necesita instalar paquetes adicionales.

## Ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

En Windows también puedes usar `py main.py`.

## Menú

1. **Traducir una palabra:** aplica las reglas y guarda la pareja original/traducción en el diccionario local.
2. **Traducir una frase:** aplica las reglas a cada palabra, convierte los signos configurados, conserva los espacios y no guarda la frase.
3. **Mostrar diccionario:** consulta las traducciones guardadas en este equipo.
4. **Salir.**

## Personalizar letras y signos

En `alfabeto.py`, cada clave representa un carácter original y cada valor es la pieza que lo reemplaza. Además de las letras, el alfabeto inicial incluye estos signos:

| Carácter | Pieza secreta |
|---|---|
| ¿ | `in` |
| ? | `chi` |
| ¡ | `ex` |
| ! | `pla` |
| . | `fin` |
| , | `kom` |

Para añadir otro signo, incorpora una nueva equivalencia de un solo carácter en `ALFABETO`. En una frase, los signos configurados se convierten sin pasar por las reglas de palabra. Los espacios y los signos que no estén configurados se conservan.

## Archivos principales

- `main.py`: menú.
- `alfabeto.py`: equivalencias entre letras, signos y piezas secretas.
- `traductor.py`: proceso de traducción y detección automática de reglas.
- `diccionario.py`: almacenamiento JSON persistente.
- `reglas/`: tres reglas de ejemplo que el traductor detecta automáticamente.
- `plantillas/`: tres ejercicios incompletos para que los estudiantes creen reglas nuevas.
- `GUIA_REGLAS_PARA_ESTUDIANTES.md`: ideas de reglas agrupadas a partir de las propuestas del aula.

## Tres reglas de ejemplo incluidas

- `reglas/regla_prefijo.py`: añade el prefijo propuesto por un estudiante. Se puede cambiar o desactivar.
- `reglas/regla_reemplazar_z.py`: cambia una pieza que sea exactamente `z` por `0`. No altera una sílaba como `zu`. En el alfabeto inicial, la letra original Z se convierte en la pieza `z`, así que la regla transforma esa pieza en `0`.
- `reglas/regla_longitud.py`: valida el mínimo y máximo de caracteres de la palabra secreta. El máximo inicial es 20 y se puede ajustar.

## Crear una regla nueva

1. Abre una plantilla de `plantillas/` o crea un archivo directamente dentro de `reglas/`.
2. El archivo debe comenzar con `regla_`, declarar `ACTIVA` y `TIPO`, e incluir la función adecuada.
3. Las transformaciones usan `aplicar(piezas, palabra_original)` y devuelven una lista de piezas.
4. Las validaciones usan `validar(piezas, palabra_original)`: devuelven `None` si la palabra cumple la regla o un mensaje de error si no la cumple.
5. Guarda el archivo y vuelve a ejecutar el programa. El traductor lo detectará; no necesitas modificar `main.py`, `traductor.py` ni `diccionario.py`.

`ORDEN` es opcional. Si no aparece, el traductor usa 50. Las transformaciones se ejecutan primero y luego las validaciones; dentro de cada fase, las reglas se ordenan por número ascendente.

**Importante:** los archivos de `plantillas/` son ejercicios incompletos y no se cargan automáticamente. Copia uno a `reglas/`, cambia su nombre para que empiece por `regla_`, completa el código y cambia `ACTIVA = False` a `True` cuando esté listo.

## Persistencia

Las traducciones se guardan en `datos/diccionario.json` y se conservan al cerrar y volver a ejecutar el programa en el mismo equipo. El archivo real se excluye de Git para no subir los datos locales.
