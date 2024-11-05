'''
Alguns corais dobram de tamanho a cada dia. Calcular o tamanho dos corais a partir de seu tamanho inicial e tempo passado.
'''

def coraisLength(ini, days):
    if days == 1:
        return ini*2
    else:
        return 2 *  coraisLength(ini, days-1)

print(coraisLength(1, 5))