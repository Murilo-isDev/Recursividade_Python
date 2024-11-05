'''
Questão de prova

O jovem Anastassius começou a trabalhar em uma lanchonete.
A lanchonete é conhecida por fazer um suco de laranja com a quantidade certa de polpa.
Como existem diversas jarras na lanchonete, o proprietário criou uma medida que para cada 10 ml de
líquido deve ser colocada uma embalagem de polpa que custa R$ 2,00.
Implementar um algoritmo recursivo capaz de receber o quantidade de ml da jarra e retorna o valor em R$ das polpas
utilizadas para fazer a jarra de suco.
 Sabendo que a quantidade de ml da jarra é sempre múltipla de 10.
'''

def calcularPolpa(qtdMl):
    if qtdMl == 10:
        return 2
    else:
        return 2 + calcularPolpa(qtdMl-10)


print(calcularPolpa(50))
