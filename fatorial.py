# Função que chama a si mesma durante a execução

#Probelmas que pedem recursividade podem dar trabalho ao tentar resolver de outra forma

# Iterativo
'''
def calcularFatorial(num):
    r=1
    for i in  range(1,num+1):
        r = r * i
    return r

num = int(input('Digite o numero para ser passado para fatorial:'))
print(calcularFatorial(num))
'''
# Com recursividade -
#Caso básico = valor que não tem mais o que fazer
def calcularFatorial(num):
    if num == 1:  # o 1 seria o caso básico
        return num
    else:
        return num * calcularFatorial(num-1)

num = int(input('Digite o numero para ser passado para fatorial:'))
print(calcularFatorial(num))