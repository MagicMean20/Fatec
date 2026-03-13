sal=0
while sal <= 0:
    sal = float(input("Digite o salário do funcionário: "))
liq = sal *1.15
print("O novo salário do funcionário é: R$ {:.2f}".format(liq))