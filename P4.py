# DEBEN DE PONERLE ANOTACION DE TIPO A TODAS LAS FUNCIONES
# 4.	Haz un menú que le permita al usuario: (10%)
# a.	Agregar términos a un polinomio
# b.	Imprimir el polinomio generado hasta el momento
# c.	Imprimir la integral del polinomio generado hasta el momento
# d.	Evaluar la expresión para un valor específico de x
# e.	Salir del menú
from typing import List, Tuple

import P2
import P3


def evalua_pol(polinomio: List[Tuple[float, float]], x: float) -> float:
    res = 0
    for t in polinomio:
        a = t[0]
        n = t[1]
        res += a * (x**n)
    return res


def main():
    polinomios = []
    while True:
        print("a.	Agregar términos a un polinomio")
        print("b.	Imprimir el polinomio generado hasta el momento")
        print("c.	Imprimir la integral del polinomio generado hasta el momento")
        print("d.	Evaluar la expresión para un valor específico de x")
        print("e.	Salir del menú")
        opcion = input("Digite opcion: ").lower().strip()
        if opcion == 'a':
            a = float(input("Digite a: "))
            n = float(input("Digite n: "))
            t = (a, n)
            polinomios.append(t)
        elif opcion == 'b':
            print(P3.conv_str(polinomios))
        elif opcion == 'c':
            print(P3.conv_str(P2.integra_polinomio(polinomios)))
        elif opcion == 'd':
            x = float(input("Digite x: "))
            print(evalua_pol(polinomios, x))
        elif opcion == 'e':
            break


if __name__ == '__main__':
    main()
