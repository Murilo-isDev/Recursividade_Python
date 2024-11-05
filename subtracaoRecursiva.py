""" Implementar a operação de subtração de forma recursiva!
"""

def subtracaoRecursiva(n1, n2):
    if n2 == 0:
        return n1
    else:
        return subtracaoRecursiva(n1-1, n2-1)

print(subtracaoRecursiva(8,4))