from bissexto import bissexto

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