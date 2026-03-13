larg=0
alt=0
comp=0
while larg <= 0 or alt <=0 or comp <= 0:
    larg = int(input("Digite a largura da figura: "))
    alt = int(input("Digite a altura da figura: "))
    comp = int(input("Digite o comprimento da figura: "))

volume = larg * alt * comp

print("O volume da figura é: ", volume)