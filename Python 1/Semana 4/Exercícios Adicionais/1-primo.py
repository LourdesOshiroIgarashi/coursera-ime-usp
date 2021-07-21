num = int(input())

aux = 2
primo = 1

while aux < num and primo == 1:
    if num % aux == 0:
        print('não primo')
        primo = 0
    else:
        aux += 1

if primo == 1:
    print('primo')
