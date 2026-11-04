"""Equivalencias editables de letras y signos a piezas del idioma secreto."""

# Cada clave representa un carácter original y cada valor, una pieza secreta.
# Puedes cambiar las equivalencias o añadir otros signos de puntuación.
ALFABETO = {
    "A": "ka",
    "B": "zu",
    "C": "mi",
    "D": "lo",
    "E": "te",
    "F": "ra",
    "G": "vi",
    "H": "no",
    "I": "sa",
    "J": "pu",
    "K": "ke",
    "L": "di",
    "M": "ma",
    "N": "re",
    "Ñ": "nya",
    "O": "to",
    "P": "lu",
    "Q": "chi",
    "R": "so",
    "S": "na",
    "T": "fe",
    "U": "ri",
    "V": "ko",
    "W": "ya",
    "X": "xe",
    "Y": "do",
    "Z": "z",  # La regla de reemplazo convierte esta pieza en 0.

    # Signos de puntuación: se convierten en frases, pero no reciben
    # las reglas que están diseñadas para transformar o validar palabras.
    "¿": "in",
    "?": "chi",
    "¡": "ex",
    "!": "pla",
    ".": "fin",
    ",": "kom",
}


def normalizar_letra(letra):
    """Convierte vocales acentuadas a su forma base; conserva la Ñ."""
    letra = letra.upper()
    if letra == "Ñ":
        return "Ñ"

    equivalencias = {
        "Á": "A", "À": "A", "Ä": "A",
        "É": "E", "È": "E", "Ë": "E",
        "Í": "I", "Ì": "I", "Ï": "I",
        "Ó": "O", "Ò": "O", "Ö": "O",
        "Ú": "U", "Ù": "U", "Ü": "U",
    }
    return equivalencias.get(letra, letra)
