a=0
b=0
c=0
while a <=0 or b <= 0 or c <= 0:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))

def baskara():
    j = b*b-4*a*c

    if j >= 0:
            if j == 0:
                r1 = (-b+(j)**(1/2))/(2*a)
                return "1 raíz real"
            else:
                r1 = (-b+(j)**(1/2))/(2*a)
                r2 = (-b-(j)**(1/2))/(2*a)
            return "2 raízes reais"
    else:
        return "Nenhuma raíz real"

print(baskara())