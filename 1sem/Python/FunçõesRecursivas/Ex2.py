# N + (N-1) + (N-2) + ... + 1

def soma(n,c,t):
    while (n-c != 0):
        t += n-c
        c+=1
        soma(n,c,t)
    t += 1 # parte final do resultado
    return t

def main():
    n = int(input("Digite um valor para a somatória de N: "))
    t=n
    c=1
    print(soma(n,c,t))

if __name__ == '__main__':
    main()