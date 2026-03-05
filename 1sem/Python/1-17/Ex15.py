cat1 = float(input("Digite a medida do cateto oposto: "))
cat2 = float(input("Digite a medida do cateto adjacente: "))

hip = (cat1 ** 2 + cat2 ** 2) ** 0.5
print(f"A medida da hipotenusa é: {hip}")