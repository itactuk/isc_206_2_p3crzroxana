# DEBEN DE PONERLE ANOTACION DE TIPO A TODAS LAS FUNCIONES
# 3.	Cree una función que dada una lista de tuplas retorne un string
# que represente la expresión como un polinomio (6%)
from typing import List, Tuple


def conv_str(lista: List[Tuple[float, float]]) -> str:
    represantacion = ""
    for t in lista:
        a = t[0]
        n = t[1]
        ts = f"{a}x{n}+"
        represantacion += ts
    return represantacion[:-1]
