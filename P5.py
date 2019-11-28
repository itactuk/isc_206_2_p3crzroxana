# DEBEN DE PONERLE ANOTACION DE TIPO A TODAS LAS FUNCIONES
# 5.	Crea una función que calcule la desviación estándar de una lista que representa la población completa (6%)
from typing import List


def desv_std(lista: List[float]) -> float:
    desv = 0
    promedio = sum(lista)/len(lista)
    for xi in lista:
        desv += (xi - promedio) ** 2

    desv = (desv/(len(lista)-1)) ** 0.5
    return desv


if __name__ == '__main__':
    print(desv_std([23,43, 532]))
