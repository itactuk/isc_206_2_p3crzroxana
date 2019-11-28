from typing import List, Tuple

import P1
# DEBEN DE PONERLE ANOTACION DE TIPO A TODAS LAS FUNCIONES
# 2.	Crea una función que integre un polinomio (a0+a1x+a2x2+a3x3+...+anxn).
# El parámetro de esta función debe de ser una lista que contenga muchas tuplas que representan c/u de los términos
# del polinomio. Recomendación: usar función del punto anterior. (6%)


def integra_polinomio(pol: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    polinomio_integrado = []
    for t in pol:
        ti = P1.integra_termino(t)
        polinomio_integrado.append(ti)
    return polinomio_integrado
