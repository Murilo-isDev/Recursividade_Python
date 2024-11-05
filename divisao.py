""" Implementar a operação de divisão de forma recursiva!
"""
def divisaoRecursiva(n1, n2):
    if n1<n2:
        return n1
    else:
        return 1 + divisaoRecursiva(n1-n2, n2)

print(divisaoRecursiva(5,20))