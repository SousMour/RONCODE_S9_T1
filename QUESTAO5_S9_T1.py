#Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco).
#A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:
#• Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
#• Se 1 (um), escreva se o valor lido é par ou ímpar;
#• Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
#• Se 3 (três), escreva a divisão inteira do valor lido por 10;
#• Se 4 (quatro), escreva o quadrado do valor lido;

def divisao_5(n):
    div = n % 5 
    if div == 0:
        print(f'{9 * n+ 7 }')
    elif div == 1:
        if n % 2 == 0:
            print('par')
        elif n % 2 != 0:
            print('ímpar')
    elif div == 2:
        print(f'{(5 * ( n * n)) - (3 * n) + 42 }')
    elif div == 3:
        print(f'{n // 10}')
    elif div == 4:
        print(f'{n ** 2}')
n=int(input())
resultado=divisao_5(n)