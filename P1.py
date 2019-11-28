# DEBEN DE PONERLE ANOTACION DE TIPO A TODAS LAS FUNCIONES
# 1.	Cree una función que integre un término de un polinomio (axn).
#  La función debe de recibir una tupla cuyo primer elemento sea el coeficiente (a) y
#  el segundo sea el exponente (n).
#  La función debe de retornar una tupla cuyo primer elemento sea a/(n+1) y su segundo elemento sea n+1,
#  es decir (a/(n+1))*Xn+1, el resultado de integrar axn. (6%)
# Por ejemplo, si a la función se le pasa la tupla (8,3), la función debe de retornar la tupla (2,4).
# Esto es por que la integral de (8x3) es (2x4)
# la función no debe de contemplar el caso 1/x
from typing import Tuple


def integra_termino(termino: Tuple[float, float]) -> Tuple[float, float]:
    a = termino[0]
    n = termino[1]
    ai = a/(n+1)
    ni = n+1
    return (ai, ni)
