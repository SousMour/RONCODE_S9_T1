#Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. 
# O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. 
# Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. 
#Separe esses valores com um hífen.

def quadrado(lado_1, lado_2):
    if lado_1 == lado_2:
        print('QUADRADO')
    elif lado_1 != lado_2:
        perimetro= 2* lado_1 + 2 * lado_2
        area = lado_1 * lado_2
        print(f'{perimetro} - {area}')

lado_1= int(input())
lado_2= int(input())
resultado = quadrado(lado_1, lado_2)