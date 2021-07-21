largura = int(input())
altura = int(input())

for i in range(altura):
    if i == 0 or i == altura - 1:
        print(largura * "#")
    else:
        n = largura - 2
        print("#",end= "")
        print(n * " ", end="")
        print("#")
