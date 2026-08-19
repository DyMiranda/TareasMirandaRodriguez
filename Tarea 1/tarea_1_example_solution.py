"""
Solución de la Tarea 1 - Punto 3.

Implementa las funciones requeridas para filtrar caracteres de una cadena
y encontrar los valores extremos de una lista. Ambas funciones retornan
códigos de estado para indicar éxito o el tipo de error detectado.
"""


def filtrar_vocales(cadena, bandera):
    """
    Filtra las vocales o consonantes de una cadena, según el valor de bandera.

    Parámetros:
        cadena (str): texto compuesto únicamente por letras y con un máximo
        de 30 caracteres.
        bandera (bool): True para retornar vocales y False para retornar
        consonantes.

    Retorna:
        tuple: código de estado y cadena filtrada.
        Si ocurre un error, retorna el código correspondiente y None.
    """

    # Validar los parámetros antes de realizar el filtrado.
    if not isinstance(cadena, str):
        return -100, None

    if cadena == "":
        return -300, None

    if not cadena.isalpha():
        return -200, None

    if len(cadena) > 30:
        return -400, None

    if type(bandera) is not bool:
        return -500, None

    vocales = "aeiouAEIOU"

    # Conservar el orden original de los caracteres al aplicar el filtro.
    if bandera:
        resultado = "".join(
            letra for letra in cadena if letra in vocales
        )
    else:
        resultado = "".join(
            letra for letra in cadena if letra not in vocales
        )

    # El código 0 indica que la operación terminó correctamente.
    return 0, resultado


def encontrar_extremos(lista_numeros):
    """
    Encuentra el valor mínimo y máximo de una lista de números.

    Parámetros:
        lista_numeros (list): lista de valores enteros o decimales, con un
        máximo de 15 elementos.

    Retorna:
        tuple: código de estado, valor mínimo y valor máximo.
        Si ocurre un error, retorna el código correspondiente y dos valores
        None.
    """

    # Validar la estructura y el contenido antes de buscar los extremos.
    if not isinstance(lista_numeros, list):
        return -600, None, None

    # Los booleanos se excluyen explícitamente aunque Python los trate
    # internamente como una subclase de int.
    if any(
        isinstance(numero, bool)
        or not isinstance(numero, (int, float))
        for numero in lista_numeros
    ):
        return -700, None, None

    if len(lista_numeros) == 0:
        return -800, None, None

    if len(lista_numeros) > 15:
        return -900, None, None

    # Con las validaciones superadas, se calculan los extremos de la lista.
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    # El código 0 indica que la operación terminó correctamente.
    return 0, minimo, maximo