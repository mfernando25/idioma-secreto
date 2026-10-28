"""Configuración de las reglas del idioma secreto.

Cambia los valores de esta sección para activar, desactivar o ajustar reglas.
"""

# Regla de transformación: añade esta pieza al inicio de cada palabra.
ACTIVAR_PREFIJO = True
PREFIJO = "pe"

# Regla de validación: no permite dos piezas iguales una junto a la otra.
ACTIVAR_SIN_REPETICIONES_CONSECUTIVAS = True

# Regla de validación: limita la longitud de la palabra traducida.
# Ejemplo: 5 permite hasta 5 caracteres traducidos por cada letra original.
ACTIVAR_LONGITUD_MAXIMA = True
MAX_CARACTERES_POR_LETRA = 5
