
""" Implementar a operação de portenciação de forma recursiva!
"""
def potenciaRecursiva(n1, n2):
    if n2 == 1:
        return n1
    else:
        return n1 * potenciaRecursiva(n1, n2-1) #o parenteses não é valor

print(potenciaRecursiva(2,5))