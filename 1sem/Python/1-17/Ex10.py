r1=0
r2=0
while r1 <= 0 or r2 <= 0:
    r1 = float(input("Digite um número: "))
    r2 = float(input("Digite outro número: "))

d = r1 - r2

if d < 0:
    print("A diferença é de {:.2f}.".format(d*(-1)))
elif d == 0:
    print("A diferença é 0")
else:
    print("A diferença é de {:.2f}.".format(d))