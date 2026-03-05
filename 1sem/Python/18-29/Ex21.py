nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 3:
    print("RETIDO")

elif media >= 3 and media < 6:
    print("EXAME")

else:
    print("APROVADO")