salario = float(input("Informe o salário: "))
tempo = int(input("Informe o tempo em anos: "))

bonus = None
if tempo >= 5:
    bonus = salario * (20/100)
else:
    bonus = salario * (10/100)

print(bonus)
