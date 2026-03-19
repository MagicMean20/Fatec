a=0
b=0
c=0
d=0
while a <= 0 or b <= 0 or c <= 0 or d <= 0:
    a = int(input("Digite um número pequeno: "))
    b = int(input("Digite um número maior que o anterior: "))
    c = int(input("Digite um número ainda maior: "))
    d = int(input("Insira qualquer número agora:"))

def ordem():
    if d < a:
        return f"A ordem é: {d}, {a}, {b}, {c}"
    elif d < b:
        return f"A ordem é: {a}, {d}, {b}, {c}"
    elif d < c:
        return f"A ordem é: {a}, {b}, {d}, {c}"
    else:
        return f"A ordem é: {a}, {b}, {c}, {d}"
    
print(ordem())