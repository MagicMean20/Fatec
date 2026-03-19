nota1=0
nota2=0
nota3=0
nota4=0
while nota1 <= 0 or nota2 <= 0 or nota3 <= 0 or nota4 <= 0:
    nota1 = float(input("Digite a nota do primeiro bimestre: "))
    nota2 = float(input("Digite a nota do segundo bimestre: "))
    nota3 = float(input("Digite a nota do terceiro bimestre: "))
    nota4 = float(input("Digite a nota do quarto bimestre: "))

def media():
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media < 3:
        return "RETIDO"

    elif media >= 3 and media < 6:
        return "EXAME"

    else:
        return "APROVADO"
    
print(media())