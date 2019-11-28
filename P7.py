# DEBEN DE PONERLE ANOTACION DE TIPO A TODAS LAS FUNCIONES

# 7.	Implemente una función que cuente la frecuencia de palabras en una lista.
# La función debe de recibir una lista
# y retornar un diccionario con la palabra (en minúscula) como llave y la cantidad de ocurrencias como valor.
# No se debe de distinguir entre mayúsculas y minúsculas. Cada elemento de la lista es una palabra (6%)
# Ejemplo:
# Entrada: [“hola”, “Hola”, “BYE”]
# Salida: {“hola”: 2, “bye”: 1}
from typing import List, Dict


def cuenta_palabras(lista_palabras: List[str]) -> Dict[str, int]:
    res = {}
    for palabra in lista_palabras:
        palabra = palabra.lower()
        if palabra not in res:
            res[palabra] = 0
        res[palabra] += 1
    return res

