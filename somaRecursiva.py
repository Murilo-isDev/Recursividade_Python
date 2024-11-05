""" Implementar a operação de soma de forma recursiva!
"""
def somaRecursiva(n1, n2):
    if n2 == 0:
        return n1
    else:
        return  somaRecursiva(n1+1, n2-1)

print(somaRecursiva(8,4))