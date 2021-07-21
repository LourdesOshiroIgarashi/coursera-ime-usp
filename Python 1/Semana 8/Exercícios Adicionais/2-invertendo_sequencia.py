lista = []

num = int(input("Digite um número: "))

while num != 0:
    lista.append(num)

    num = int(input("Digite um número: "))

for i in lista[::-1]:
    print(i)
