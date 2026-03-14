voltas=0
tam=0
min=0
while voltas <= 0 or tam <= 0 or min <= 0:
    voltas = int(input("Informe as voltas feitas: "))
    tam = int(input("Qual o tamanho do circuito:"))
    min = int(input("Quantos minutos levou: "))

vmpm = int(voltas * tam / min)
print(vmpm, " metros por minuto")

# km/h
kmh = vmpm * 3.6
print(kmh, "km/h")