dec=0
while dec <= 0:
    dec = int(input("Digite um número: "))
s = 1
d = dec

while dec > 1:
    s = s + s/dec
    dec = dec - 1

print("O resultado da soma de 1 até", d, "parte (1/n) é: ", s)