""" Mostrar toda a sequência para fazer o calculo do fatorial como string!
"""

def fatorial(n):
    if n == 1:
        return '1'
    else:
        return  str(n) + 'x' + fatorial(n-1)

print(fatorial(5))