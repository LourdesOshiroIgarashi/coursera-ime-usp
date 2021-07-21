#  Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.
#  Para a saída, siga o formato do exemplo abaixo.

n = int(input())

aux = 1
num = 1

while aux <= n:
    print(num)
    num += 2
    aux += 1
