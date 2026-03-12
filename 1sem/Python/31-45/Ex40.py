# Terminar
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    c = n1
    n1 = n2
    n2 = c

if n1 > 1 or n2 > 1:
    print("Números primos entre", n1, "e", n2, ":")
    for num in range(n1, n2 + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)
else:
    print("Digite números maiores que 1.")