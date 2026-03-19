n1 = int(input("Informe um número: "))
n2 = int(input("Dê outro número: "))

def maioredivisivel():
    if n1 > n2:
        som = n1 % n2
        if som == 0:
            return f"{n1} é maior que {n2} e também é divisível"
        else:
            return f"{n1} é maior que {n2}"
    elif n2 > n1:
        som = n2 % n1
        if som == 0:
            return f"{n2} é maior que {n1} e também é divisível"
        else:
            return f"{n2} é maior que {n1}"
    else:
        return "Números iguais"