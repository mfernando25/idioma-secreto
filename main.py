"""Programa principal del creador de un idioma secreto."""

import diccionario
from traductor import traducir_frase, traducir_palabra


def opcion_traducir_palabra():
    palabra = input("Escribe una palabra: ").strip()

    traduccion, error = traducir_palabra(palabra)
    if error:
        print(f"\nNo se pudo traducir: {error}")
        print("La palabra no se guardó en el diccionario.\n")
        return

    try:
        diccionario.registrar_traduccion(palabra, traduccion)
    except (OSError, ValueError) as error_guardado:
        print(f"\nLa traducción es: {traduccion}")
        print(f"No se pudo guardar en el diccionario: {error_guardado}\n")
        return

    print(f"\nPalabra original: {palabra}")
    print(f"Palabra secreta:  {traduccion}")
    print("La traducción se guardó en el diccionario.\n")


def opcion_traducir_frase():
    frase = input("Escribe una frase: ").strip()
    if not frase:
        print("Escribe una frase antes de continuar.\n")
        return

    frase_traducida, errores = traducir_frase(frase)
    print(f"\nFrase original:  {frase}")
    print(f"Frase traducida: {frase_traducida}")

    if errores:
        print("\nAlgunas palabras se conservaron en su forma original:")
        for palabra, motivo in errores:
            print(f"- {palabra}: {motivo}")

    print("\nLa frase no se guardó en el diccionario.\n")


def opcion_mostrar_diccionario():
    try:
        entradas = diccionario.obtener_entradas()
    except (OSError, ValueError) as error:
        print(f"\nNo se pudo leer el diccionario: {error}\n")
        return

    print("\n--- DICCIONARIO DEL IDIOMA SECRETO ---")
    if not entradas:
        print("Todavía no hay traducciones guardadas.\n")
        return

    for entrada in entradas:
        print(f"{entrada['original']}  ->  {entrada['traduccion']}")
    print()


def mostrar_menu():
    print("=== CREADOR DE IDIOMA SECRETO ===")
    print("1. Traducir una palabra")
    print("2. Traducir una frase")
    print("3. Mostrar diccionario")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()
        print()

        if opcion == "1":
            opcion_traducir_palabra()
        elif opcion == "2":
            opcion_traducir_frase()
        elif opcion == "3":
            opcion_mostrar_diccionario()
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 4.\n")


if __name__ == "__main__":
    main()
