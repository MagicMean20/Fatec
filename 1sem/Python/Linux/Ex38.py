import os

global dir,arq,min,max,linha
dir='/home/henrique/Download/exercicios/'
arq='Ex38.txt'
linha=''
min=0
max=0

def entra(c):
    global min,max
    n = ''
    for abc in range(10):
        # num está como string pois há no código uma verificação para impedir espaços em branco,
        # substituindo por 0, e isso não é possível se num for um inteiro
        num='-1' 
        while int(num) < 0:
            num = input(f"Digite um número({abc+1}): ")
            if num == '':
                num = '0'
            if int(num) < 0:
                print("Número inválido. Digite um número maior que 0.")
                continue
        if (c == 0 and abc == 0):
            max = int(num)
            min = int(num)
        else:
            if (int(num) > max):
                max = int(num)
            if (int(num) < min):
                min = int(num)
        n += num + '; '
        if abc == 9:
            grava(min,max,n,abc,c)

def grava(min,max,num,a,c):
    global dir,arq,linha
    file = dir + arq
    linha = ''

    enc='utf-8'
    if (c != 9):
        linha += num
    else:
        linha += num + '\n'
        linha += 'Min: ' + str(min) + ' // Max: ' + str(max)
    
    if (os.path.isdir(dir) and os.path.exists(dir)):
        tipo = 'w'
        if (os.path.exists(file)):
            tipo='a'
        with open(file,tipo,encoding=enc) as f:
            f.write(linha + '\n')

def main():
    global dir,linha
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir,0o744)

    for cont in range(10):
        entra(cont)
        print(f'Dezena de dígitos confirmada ({cont+1})')
        linha = ''

# lembrar de trocar os range 2 e elif 2 por 11
# tentar realocar a lógica de gravação pq n tá aparecendo o min e max no arquivo

if __name__ == "__main__":
    main()