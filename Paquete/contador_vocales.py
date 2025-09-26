def contar_vocales(frase):
    """
    Cuenta cuántas veces aparece cada vocal en la frase.

    Args:
        frase (str): Texto a analizar.

    Returns:
        dict: Diccionario con las vocales como claves y la cantidad de apariciones como valores.
    """
    frase = frase.lower()
    vocales = "aeiou"
    conteo = {v: 0 for v in vocales}
    for letra in frase:
        if letra in vocales:
            conteo[letra] += 1
    return conteo
