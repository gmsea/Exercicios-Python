salario = float(input('digite o seu salario em R$'))
if salario > 1250:
    s1 = salario * 1.1
    print(f'Seu salário foi aumentado para R${s1:.2f}')
else:
    s2 = salario * 1.15
    print(f'Seu salário foi aumentado para R${s2:.2f}')