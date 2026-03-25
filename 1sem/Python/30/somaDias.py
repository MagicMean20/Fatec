from diasMes import diasMes

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

    print("Você tem",anoI,"anos",mesI,"meses e",diaI,"dias")