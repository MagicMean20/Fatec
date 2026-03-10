# Horas e minutos separdos
Hini = int(input("Insira as horas do início do jogo: "))
Mini = int(input("Insira os minutos do início do jogo: "))
Hfim = int(input("Qual a hora do fim do jogo: "))
Mfim = int(input("Quantos minutos do fim do jogo: "))

Hjogo = Hfim - Hini
Mjogo = Mfim - Mini

if Hjogo < 0:
    Hjogo = Hjogo * -1
if Mjogo < 0:
    Mjogo = Mjogo * -1

if Hjogo < 23 and Mjogo < 59:
    print(f"O jogo está permitido, tendo duração de {Hjogo}:{Mjogo}.")
else:
    print("O jogo não pode acontecer.")