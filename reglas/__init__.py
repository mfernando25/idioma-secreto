"""Reglas detectadas automáticamente por el traductor.

Cada archivo debe llamarse regla_nombre.py y declarar:
ACTIVA = True o False
TIPO = "transformacion" o "validacion"
ORDEN = un número entero

Las reglas de transformación implementan aplicar(piezas, palabra_original).
Las reglas de validación implementan validar(piezas, palabra_original).
"""
