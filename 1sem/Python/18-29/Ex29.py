tipo = int(input("Tipo de Investimento:\n" \
             "1 - Poupança\n" \
             "2 - Renda Fixa\n" \
             "Digite o tipo desejado: "))

if tipo == 1 or tipo == 2:
    if tipo == 1:
        taxa = 0.03
    else:
        taxa = 0.05
    
    valor = float(input("Valor a ser investido: "))
    
    valorF = valor + (valor * taxa)
    print(f"Valor final do investimento: R${valorF:.2f}")
else:
    print("Tipo de investimento inválido.")


