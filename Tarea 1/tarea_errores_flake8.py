CODIGOEXITO = 0
ERROR_NO_STRING = -100
ERROR_NO_SOLO_LETRAS = -200
ERROR_STRING_VACIO = -300
ERROR_STRING_LARGO = -400
ERROR_NO_BOOLEANO = -500
ERROR_NO_LISTA = -600
ERROR_ELEMENTOS_NO_NUMERICOS = -700
ERROR_LISTA_VACIA = -800
ERROR_LISTA_LARGA = -900
# Funcion para filtrar vocales


def filtrar_vocales(cadena, bandera):
    # Error en caso de que el parámetro no sea un string
    if not isinstance(cadena, str):
        return ERROR_NO_STRING, None
    # Error en caso de que el parámetro sea un string vacio
    if cadena == "":
        return ERROR_STRING_VACIO, None
    # Error en caso que el string contenga caracteres fuera del alfabeto
    if not cadena.isalpha():
        return ERROR_NO_SOLO_LETRAS, None
    # Error en caso de que el string tenga más de 30 caracteres
    if len(cadena) > 30:
        return ERROR_STRING_LARGO, None
    # Error en caso de que bandera no sea un booleano
    if not isinstance(bandera, bool):
        return ERROR_NO_BOOLEANO, None

    # Se definen las letras vocales
    vocales = "aeiouAEIOU"
    # Si la bandera es true se filtran las vocales
    if bandera:
        resultado = "".join([c for c in cadena if c in vocales])
    # Si la bandera es false se filtran las consonantes
    else:
        resultado = "".join([c for c in cadena if c not in vocales])
    return CODIGOEXITO, resultado


# Funcion para encontrar maximo y minimo en una lista de numeros
def encontrar_extremos(lista_numeros):
    # Error en caso de que el parámetro no sea una lista
    if not isinstance(lista_numeros, list):
        return ERROR_NO_LISTA, None, None
    # Error en caso de que la lista esté vacía
    if len(lista_numeros) == 0:
        return ERROR_LISTA_VACIA, None, None
    # Error en caso de que haya algo distinto a un int o float en la lista
    # Errores por multiples statements y exceso de caracteres
    if not all(isinstance(x, (int, float)) for x in lista_numeros):
        return ERROR_ELEMENTOS_NO_NUMERICOS, None, None
    # Error en caso de que la lista tenga más de 15 elementos
    if len(lista_numeros) > 15:
        return ERROR_LISTA_LARGA, None, None
    # Si no hay errores se encuentra y retorna el minimo y maximo de la lista
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    return CODIGOEXITO, minimo, maximo
