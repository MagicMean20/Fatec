val=0
while val <= 0:
    val = int(input("Digite um número:"))

def divisivel():
    if val % 2 == 0 and val % 3 == 0:
        return "O valor é divisível por 2 e 3"
    else:
        return "O valor não é divisível por 2 e 3"
    
print(divisivel())