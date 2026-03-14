N=0
while N <= 0:
    N = int(input("Digite um valor: "))
N-=3
A = 1
B = 1
F = 1
print("0")
print(A)
print(B)
while N != 0:
    C = A+B
    print(C)
    N-=1
    if F%2==0:
        A=C
        F+=1
    else:
        B=C
        F+=1
        # TODO: write code...