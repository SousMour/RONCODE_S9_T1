#Escreva um programa que leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 
# 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). 
# Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

def calcular(valor_1,valor_2, operacao):
    if operacao == 1:
        adicao= valor_1 + valor_2
        print(f'{adicao}')
    elif operacao == 2:
        subtracao=valor_1 - valor_2
        print(f'{subtracao}')
    elif operacao == 3:
        multi= valor_1 * valor_2
        print(f'{multi}')
    elif operacao == 4:
        divi=valor_1 / valor_2
        print(f'{divi:.2f}')
    else:
        print('Operação inválida!')

valor_1=int(input())
valor_2=int(input())
operacao=int(input())
resultado=calcular(valor_1, valor_2,operacao)