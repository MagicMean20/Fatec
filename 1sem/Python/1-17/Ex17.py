tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
vel = float(input("Digite a velocidade média durante a viagem (em km/h): "))

dist = tempo * vel
litros = dist / 12

print(f"A quantidade de litros de combustível gasta na viagem é: {litros:.2f} litros.")