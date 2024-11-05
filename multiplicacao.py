
""" Implementar a operação de multiplicação de forma recursiva!
"""
def multiplicacaoRecursiva(n1, n2):
    if n2 == 1:
        return n1
    else:
        return n1 + multiplicacaoRecursiva(n1, n2-1)

print(multiplicacaoRecursiva(3,4))