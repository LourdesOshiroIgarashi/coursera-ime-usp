y = int(input())


def n_primos(n):
    divisor = 1
    cont = 0
    while divisor <= n:
        if n % divisor == 0:
            cont = cont + 1
        divisor = divisor + 1
    primo = 0
    if cont == 2:
        primo += 1
    return primo


x = n_primos(y)
print(x)
