ano=0
atual=0
while ano <= 0 or atual <= 0:
    ano = int(input("Digite seu ano de nascimento: "))
    atual = int(input("Digite o ano atual: "))

idade = atual - ano

an17 = idade + 17

print("Sua idade é: ", idade)
print("Você terá ", an17, " em 17 anos.")