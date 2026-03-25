global anoI,mesI,diaI
anoI=0
mesI=0
diaI=0

def bissexto(ano:int)->int:
    if (ano % 4 == 0): 
        return 29 
    else:  
        return 28 

def validador(anoA:int,mesA:int,diaA:int,anoN:int,mesN:int,diaN:int):
    global anoI,mesI,diaI

# Validando variáveis mês e dia 
    if (mesA < 1 or mesA > 12) or (diaA < 1 or diaA > int(diasMes(mesA,anoA,mesN,anoN))): 
        return "Entrada inválida na seção Atual" 
    if (mesN < 1 or mesN > 12) or (diaN < 1 or diaN > int(diasMes(mesA,anoA,mesN,anoN))): 
        return "Entrada inválida na seção Nascimento" 

    diaI = diaA - diaN 
    anoI = anoA - anoN 
    mesI = mesA - mesN 

# Validando intervalo de tempo 
    if (anoI < 0): 
        return "Os anos não batem"
    if (anoI == 0 and mesI < 0): 
        return "Os meses não batem" 
    if (anoI == 0 and mesI == 0 and diaI < 0): 
        return "Os dias não coincidem"
    
    if mesA == 2 or mesN == 2:
        dias = diasMes(mesA,anoA,mesN,anoN)
        if (mesA == 2 and diaA > dias) or (mesN == 2 and diaN > dias):
            return "Dias de Fevereiro inválidos (ano bissexto)"
    return True

def diasMes(mesA:int, anoA:int, mesN:int, anoN:int)->int:

    match mesA:
        case 1: 
            dias = 31 
        case 2: 
            dias = int(bissexto(anoA)) 
        case 3: 
            dias = 31 
        case 4: 
            dias = 30 
        case 5: 
            dias = 31 
        case 6: 
            dias = 30 
        case 7: 
            dias = 31 
        case 8: 
            dias = 31 
        case 9: 
            dias = 30 
        case 10: 
            dias = 31 
        case 11: 
            dias = 30 
        case 12: 
            dias = 31
        case _:
            dias = 30

    match mesN:
        case 1: 
            dias = 31 
        case 2: 
            dias = int(bissexto(anoN)) 
        case 3: 
            dias = 31 
        case 4: 
            dias = 30 
        case 5: 
            dias = 31 
        case 6: 
            dias = 30 
        case 7: 
            dias = 31 
        case 8: 
            dias = 31 
        case 9: 
            dias = 30 
        case 10: 
            dias = 31 
        case 11: 
            dias = 30 
        case 12: 
            dias = 31
        case _:
            dias = 30
    
    return dias
 
def somaDias(anoA:int,mesA:int,diaA:int,anoN:int,mesN:int,diaN:int)->int:
    global anoI,mesI,diaI

    anoI = anoA - anoN 
    mesI = mesA - mesN 
    diaI = diaA - diaN 

    d = diaA - diaN	 

    if (d > 0): 
        total = d 
    elif (d < 0): 
        total = diaN - diaA

    if mesN > mesA:
        anoI-=1
        mesI= mesI + 12
    while (total > diasMes(mesA,anoA,mesN,anoN)):
        mesI += 1
        total -= diasMes(mesA,anoA,mesN,anoN) 

    diaI=total

    if mesI == 12:
        anoI+=1
        mesI=1

    return anoI,"anos",mesI,"meses e",diaI,"dias"

# Falta a lógica para implementar os valores obtidos como resultado

def __main__():
    global aa,ma,da,an,mn,dn
    print("Descubra a seguir qual sua idade em anos, meses e dias") 
    an = int(input("Digite o ano de seu nascimento: ")) 
    mn = int(input("Digite o mês de seu nascimento: ")) 
    dn = int(input("Digite o dia de seu nascimento: ")) 
    print("-"*25) 
    aa = int(input("Digite o ano atual: ")) 
    ma = int(input("Digite o mês atual: ")) 
    da = int(input("Digite o dia atual: ")) 

    if validador(aa,ma,da,an,mn,dn) == True:
        print("você tem",somaDias(aa,ma,da,an,mn,dn))
    else: 
        print(validador(aa,ma,da,an,mn,dn))

if "__name__" == __main__(): 
    __main__()