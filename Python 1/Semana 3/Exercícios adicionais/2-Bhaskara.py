import math

a = float(input())
b = float(input())
c = float(input())

d = b*b - 4 * a * c

if d == 0:
    # raíz dupla
    x1 = (- b + math.sqrt(d))/(2*a)
    print("a raiz desta equação é {0:.1f}".format(x1))

else:
    # não possui raízes reais
    if d < 0:
        print("esta equação não possui raízes reais")

    # 2 raízes reais distintas
    else:
        x1 = (- b + math.sqrt(d)) / (2 * a)
        x2 = (- b - math.sqrt(d))/(2*a)
        if x1 < x2:
            print("as raízes da equação são {0:.1f} e {1:.1f}".format(x1, x2))

        else:
            print("as raízes da equação são {0:.1f} e {1:.1f}".format(x2, x1))
