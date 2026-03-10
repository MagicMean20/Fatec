a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
soma = 0

if a < b:
    # caso a seja menor que b
    if a % 2 == 0:
        a += 1
    while soma < b:
        soma += a
        a += 2

        # para evitar que o programa imprima um valor maior que b
        if soma <= b:
            print(soma)
else:
    # caso b seja menor que a
    if b % 2 == 0:
        b += 1
    while soma < a:
        soma += b
        b += 2

        # para evitar que o programa imprima um valor maior que a
        if soma <= a:
            print(soma)