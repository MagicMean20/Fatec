a=0
b=0
c=0
while a <= 0 or b <= 0 or c <= 0:
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite outro número inteiro: "))
    c = int(input("Digite mais um número inteiro: "))

# achando o delta
delta = b**2 - 4*a*c

raiz1 = (-b + delta**0.5) / (2*a)
raiz2 = (-b - delta**0.5) / (2*a)

print("As raízes da equação são:", raiz1, "e", raiz2)