def maior_elemento(lista):
    maxv = lista[0]
    for i in lista:
        if i > maxv:
            maxv = i
    return maxv
