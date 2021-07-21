def entrada():
    return int(input())


a = entrada()
b = entrada()


def maximo(a, b):
    if a >= b:
        print(a)
    else:
        print(b)

c = maximo(a, b)
