r1=0
r2=0
while r1 <= 0 or r2 <= 0:
    r1 = float(input("Digite um número: "))
    r2 = float(input("Digite outro número: "))

d = r1 - r2

if d < 0:
    print("O resultado {:.2f}.".format(d))
else:
    print("O resultado {:.2f}.".format(d))