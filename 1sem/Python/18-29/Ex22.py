v1=0
v2=0
while v1 <= 0 or v2 <= 0:
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))

def ordem():
    if v1 > v2:
        return f"A ordem crescente dos valores é: {v2}, {v1}"
    elif v2 > v1:
        return f"A ordem crescente dos valores é: {v1}, {v2}"
    else:
        return "Valores iguais"
    
print(ordem())