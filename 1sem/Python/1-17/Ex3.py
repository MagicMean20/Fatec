base=0
altura=0
while base <=0 or altura <=0:
    base = int(input("Digite a base do triângulo: "))
    altura = int(input("Digite a altura do triângulo: "))
area = (base * altura) / 2
print("A área do triângulo é:", area)