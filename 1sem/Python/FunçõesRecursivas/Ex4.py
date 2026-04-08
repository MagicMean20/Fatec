def div(n,c,t):
    if (c < n):
        t += (n-c)/(c+1)
        div(n,c+1,t)
    print(t)

def main():
    n = int(input('Digite um valor para N: '))
    tot = n-1
    c=1
    div(n,c,tot)

if __name__ == '__main__':
    main()