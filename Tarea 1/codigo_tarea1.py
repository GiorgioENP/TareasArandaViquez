def filtrar_vocales(cadena, bandera):

    # Se definen los códigos de error únicos solicitados del inciso a-e

    no_error = 0
    error_string = 1
    error_abecedario = 2
    error_vacio = 3
    error_longitud = 4
    error_bandera = 5

    # Verificación de errores

    # a) Verifica que el tipo de dato de cadena sea string
    if not isinstance(cadena, str):
        return error_string, None

    # b) Verifica que la cadena solo contenga letras del abecedario
    if not cadena.isalpha():
        return error_abecedario, None

    # c) Verifica que la cadena no sea string vacío
    if len(cadena) == 0:
        return error_vacio, None

    # d) Verifica que la longitud de la cadena no sea mayor a 30 caracteres
    if len(cadena) > 30:
        return error_longitud, None

    # e) Verifica que el tipo de dato de bandera sea booleano
    if not isinstance(bandera, bool):
        return error_bandera, None

    # Si no se detectan errores, se procede a filtrar las vocales

    vocales = 'aeiouAEIOU'

    if bandera:
        # Genera un resultado con solo las vocales por lista por comprensión
        resultado = ''.join([letra for letra in cadena if letra in vocales])
    else:
        # Genera resultado con las consonantes por lista por comprensión
        resultado = ''.join([letra for letra in cadena if letra not in vocales])

    return no_error, resultado


def encontrar_extremos(lista_numeros):

    # Se definen los códigos de error únicos solicitados del inciso a-e

    no_error = 0
    error_lista = 1
    error_numeros = 2
    error_vacio = 3
    error_longitud = 4

    # Verificación de errores

    # a) Verifica que el tipo de dato de lista_numeros sea una lista
    if not isinstance(lista_numeros, list):
        return error_lista, None, None

    # b) Verifica que todos los elementos de la lista sean int o float
    if not all(isinstance(num, (int, float)) for num in lista_numeros):
        return error_numeros, None, None

    # c) Verifica que la lista no esté vacía
    if len(lista_numeros) == 0:
        return error_vacio, None, None

    # d) Verifica que la longitud de la lista no sea mayor a 15 elementos
    if len(lista_numeros) > 15:
        return error_longitud, None, None

    # Resultados de no encontrar errores

    maximo = max(lista_numeros)
    minimo = min(lista_numeros)

    return no_error, maximo, minimo
