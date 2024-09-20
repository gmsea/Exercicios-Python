fecha = '\033[m'
amarelo = '\033[0;33m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
print('--'*21)
print(f'-======= {amarelo}Simulador de Empréstimo{fecha} =======-')
print('--'*21)
casa = float(input('Digite o valor da CASA: '))
entrada = float(input('Quanto gostaria de dar de entrada? '))
salario = float(input('Digite o seu SALÁRIO: '))
anos = int(input('Em quantos anos gostaria de pagar? '))
parcela = casa / (anos * 12)
if (parcela) > (salario) * 0.3:
    print(f'-======= {vermelho}Simulação NEGADA{fecha} =======-')
    print(f'Desculpe, sua prestação mensal R${verde}{parcela:.2f}{fecha} fica acima do limite para seu {vermelho}salário{fecha}')
else:
    print(f'-======= {verde}Simulação APROVADA{fecha} =======-')
    print(f'Parabéns, O seu salário de R${verde}{salario:.2f}{fecha} foi aprovado para pagar a parcela de R${verde}{parcela:.2f}{fecha}')

print('Obrigado pela consulta!!!')


