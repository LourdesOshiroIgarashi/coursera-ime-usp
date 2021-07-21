# Escreva um programa que receba um número inteiro na entrada
# verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
# Caso exista, imprima "sim";
# se não existir, imprima "não"

num = int(input())

seguido = 0
aux = 0

while num != 0 and seguido == 0:
    aux = num % 10
    num = num // 10

    if aux == num % 10:
        print('sim')
        seguido = 1

if seguido == 0:
    print('nao')
