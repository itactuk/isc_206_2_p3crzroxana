# DEBEN DE PONERLE ANOTACION DE TIPO A TODAS LAS FUNCIONES

# 8.	Cree una función que dado un string (como parámetro) extraiga todos los textos
# que se encuentren entre comillas. Si hay un número impar de comillas la función debe de retornar None (6%)
# 	Ejemplo:
# 	Entrada: “hola” es una palabra, “vas bien” es otra palabra
# 	Resultado: [‘hola’,’vas bien’]
from typing import List


def extrae_comillas(txt: str) -> List[str]:
    if txt.count('"') % 2 == 1:
        return None
    res = []
    while '"' in txt:
        ii = txt.find('"')
        txt = txt[ii+1:]
        ind_f = txt.find('"')
        res.append(txt[:ind_f])
        txt = txt[ind_f+1:]
    return res
