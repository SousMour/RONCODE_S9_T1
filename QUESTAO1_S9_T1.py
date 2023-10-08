#Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os valores lidos:
#• Todos os valores são diferentes;
#• Existem dois valores iguais e um diferente;
#• Todos os valores são iguais.

def verificar(numero_1, numero_2, numero_3):
    if numero_1 == numero_2 and numero_2 == numero_3:
        print('Todos os valores são iguais')
    elif numero_1 == numero_2 or numero_2 == numero_3 or numero_1 == numero_3:
        print('Existem dois valores iguais e um diferente')
    else:
        print('Todos os valores são diferentes')

numero_1 = int(input())
numero_2 = int(input())
numero_3 = int(input())
resultado=verificar(numero_1,numero_2,numero_3)
