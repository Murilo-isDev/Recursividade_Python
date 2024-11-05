""" Implementar a operação de potenciação de forma recursiva em string!
"""
def potencia(a,b):
    if b == 1:
        return str(a)
    else:
        return str(a) + 'x' + potencia(a, b-1)

print(potencia(4,5))