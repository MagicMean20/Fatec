precoA=0
med=0
while precoA <= 0 or med <= 0:
    precoA = float(input("Digite o preço do produto atualmente: "))
    med = float(input("Digite a média de preço do produto: "))

# med        precoA     Varia     Ajuste
# <500 	      <30	       +        10%
# >=500<1000 >=30<80	   +        15%
# >=1000	  >=80	       -         5%
# Em outras condições, o preço do produto não sofre ajuste.

if med < 500 and precoA < 30:
    taxa = 0.10
    precoA += precoA * taxa
elif 500 <= med < 1000 and 30 <= precoA < 80:
    taxa = 0.15
    precoA += precoA * taxa
elif med >= 1000 and precoA >= 80:
    taxa = 0.05
    precoA -= precoA * taxa
else:
    taxa = 0

print(f"Preço ajustado: R${precoA:.2f}")