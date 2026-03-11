n = int(input("Digite um valor: "))
s = 1
total=0

while n > 1:
    C = s/n
    total += s + C
    print(n, C, total, "\n")
    n -= 1