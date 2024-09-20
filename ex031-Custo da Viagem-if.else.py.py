dis = int(input('Qual é a distacia em Km da sua viagem? '))
if dis <= 200:
    preco1 = dis * 0.5
    print(f'O valor da sua viagem fica R${preco1:.2f}\nSua viagem é curta')
else:
    preco2 = dis * 0.45
    print(f'O valor da sua viagem fica R${preco2:.2f}\nSua viagem é longa')