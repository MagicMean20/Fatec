a = int(input("Digite um número pequeno: "))
b = int(input("Digite um número maior que o anterior: "))
c = int(input("Digite um número ainda maior: "))
d = int(input("Insira qualquer número agora:"))

if d < a:
    print(f"A ordem é: {d}, {a}, {b}, {c}")
elif d < b:
    print(f"A ordem é: {a}, {d}, {b}, {c}") 
elif d < c:
    print(f"A ordem é: {a}, {b}, {d}, {c}") 
else:
    print(f"A ordem é: {a}, {b}, {c}, {d}")