# DEBEN DE PONERLE ANOTACION DE TIPO A TODAS LAS FUNCIONES
# 6.	Cree una función que calcule la suma de todos los números pares de una lista. (6%)
from typing import List


def suma_pares(lista: List[float]):
    acc = 0
    for numero in lista:
        if numero % 2 == 0:
            acc += numero
    return acc
