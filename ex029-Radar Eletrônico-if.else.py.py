import time
vel = int(input('Qual foi a velocidade aferida: '))
print('Processando...')
time.sleep(2)
if vel > 80:
    print(f'Voce foi multado pela velocidade de {vel}Km/h')
    multa = (vel - 80) * 7
    print(f'A multa ficara no valor de R${multa},00')
print('Tenha um bom dia, Dirija com segurança !!!')