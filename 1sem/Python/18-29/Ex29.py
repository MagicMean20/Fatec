tipo=0
while tipo == 0 or tipo > 2:
    tipo = int(input("Tipo de Investimento:\n" \
             "1 - Poupança\n" \
             "2 - Renda Fixa\n" \
             "Digite o tipo desejado: "))

if tipo == 1:
    taxa = 0.03
else:
    taxa = 0.05
    
valor = float(input("Valor a ser investido: "))

def calcular_investimento():
    valorF = valor + (valor * taxa)
    return f"Valor final do investimento: R${valorF:.2f}"

print(calcular_investimento())

