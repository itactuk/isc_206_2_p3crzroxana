

def obten_resultado(operador, linea):
    ops = linea.split(operador)
    op1 = float(ops[0])
    op2 = float(ops[1])
    if operador == '+':
        return op1 + op2
    if operador == '-':
        return op1 - op2
    if operador == '*':
        return op1 * op2
    if operador == '/':
        return op1 / op2
    return 0

with open('data.txt', 'r') as archivo:
    contenido = archivo.read()
    for linea in contenido.split('\n'):
        for op in "+-*/":
            if op in linea:
                resultado = obten_resultado(op, linea)
                print(resultado)
                with open('resultado.txt', 'w') as archivo_resultado:
                    archivo_resultado.write(str(resultado) + '\n')
