val1=0
val2=0
while val1 <= 0 or val2 <= 0:
    val1 = int(input("Digite o primeiro valor: "))
    val2 = int(input("Digite o segundo valor: "))

if val1 > val2:
    print(f"O maior valor é: {val1}")
elif val2 > val1:
    print(f"O maior valor é: {val2}")
else:
    print(f"valores iguais")