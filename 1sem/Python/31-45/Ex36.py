n=0
while n <= 0:
    n = int(input("Digite um valor: "))
s = 1
total=0

def somaMod(maxi,mini,res):
    while maxi > 1:
        res += mini + (mini/maxi)
        maxi -= 1
    else:
        print(res)

somaMod(n,s,total)
