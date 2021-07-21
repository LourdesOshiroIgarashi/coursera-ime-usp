import math

x = int(input())
y = int(input())
a = int(input())
b = int(input())

multi1 = (x - a) * (x - a)
multi2 = (y - b) * (y - b)
d1 = multi1 + multi2

d = math.sqrt(d1)

if d >= 10:
    print("longe")
else:
    print("perto")
