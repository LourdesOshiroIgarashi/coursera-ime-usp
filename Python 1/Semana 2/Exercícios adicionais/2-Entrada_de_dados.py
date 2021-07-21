inserido = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horas = inserido//3600
dias = horas//86400
xsegundos = inserido%3600
minutos = xsegundos//60
segundos = xsegundos%60

if (horas >=24):
    dias = int(horas/24)
    horas = int(horas%24)

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))
