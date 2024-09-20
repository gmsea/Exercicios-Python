from datetime import datetime
ano = datetime.now().year
clo = '\033[m'
yel = '\033[0;33m'
red = '\033[0;31m'
blu = '\033[0;34m'
gre = '\033[0;32m'
print(f'{gre}={clo}'* 100)
print(f'{gre}={clo}'* 100)
print(f'{yel}={clo}'* 100)
print(f'{blu}=========================== PROGRAMA DE ALISTAMENTO MILITAR OBRIGATORIO ============================{clo}')
print(f'{yel}={clo}'* 100)
print(f'{gre}={clo}'* 100)
print(f'{gre}={clo}'* 100)
nome = str(input('Informe seu nome : '))
ida = int(input('Informe sua idade: '))
if ida <= 16:
    nas = (ida - 18) * (-1)
    print(f'Ainda {red}faltam {nas} anos{clo} para voce se alistar.')
elif ida == 17:
    ani = str(input('Voce faz 18 esse ano?\nResponda com SIM ou NAO: ')).strip().upper()
    if ani == 'SIM':
        print(f'Voce {gre}esta apto{clo} para o alistamento do exercito.')
    elif ani == 'NAO':
        print(f'Voce só pode se alistar {red}ano que vem{clo}.')
elif ida == 18:
    print(f'Voce ja deve estar cadastrado para o alistamento militar, caso ja tenha cadastro , apenas aguarde ser chamado.')
elif ida > 18:
    nas = ida - 18
    print(f'Ja se {gre}passaram {nas} anos{clo} do seu alistamento obrigatorio !')
print(f'\nTenha um bom dia sr. {nome}')




