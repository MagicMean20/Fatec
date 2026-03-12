# Terminar
dado1 = 1
dado2 = 1
c = 1
acerto=0

while dado1 != 6 and dado2 != 6:
    d = dado1 + dado2
    if d != 7:
        print(f"chance{c}: {d}")
    else:
        print(f"chance{c}: {d} - ACERTOU!")
        acerto += 1

    c += 1

print(f"Chances de soma 7: {c}/{c/acerto:.2f}")