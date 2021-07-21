segundos = int(input("Digite um número em segundos"))

hor = segundos//3600
# // é o resultado inteiro da divisão
xseg = segundos % 3600
# % é o resto da divisão
min = xseg // 60
seg = xseg % 60

print("Há {} horas, {} minutos e {} segundos em {} segundos.".format(hor, min, seg, segundos))
