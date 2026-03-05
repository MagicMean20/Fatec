a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

j = b*b-4*a*c

if j >= 0:
    if j == 0:
        r1 = (-b+(j)**(1/2))/(2*a)
        print("1 raíz real")
        print(r1)
    else:
        r1 = (-b+(j)**(1/2))/(2*a)
        r2 = (-b-(j)**(1/2))/(2*a)
        print("2 raízes reais")
        print(r1)
        print(r2)
else:
    print("Nenhuma raíz real")