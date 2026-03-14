n1=0
n2=0
while n1 <= 0 or n2 <= 0:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

dif = n1 - n2

if dif < 0:
    print("O segundo número ({}) é maior que o primeiro ({}).".format(n2, n1))
elif dif > 0:
    print("O primeiro número ({}) é maior que o segundo ({}).".format(n1, n2))
else:
    print("Os números são iguais.")