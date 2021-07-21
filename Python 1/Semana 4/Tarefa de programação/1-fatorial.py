#  Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

n = int(input())

fat = 1

i = 2

while i <= n:
    fat = fat*i
    i = i + 1

print(fat)
