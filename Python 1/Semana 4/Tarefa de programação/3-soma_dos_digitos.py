#  Escreva um programa que receba um número inteiro na entrada,
#  calcule e imprima a soma dos dígitos deste número na saída

n = int(input())

soma = 0

while n != 0:
    soma += n % 10
    n = n // 10

print(soma)
