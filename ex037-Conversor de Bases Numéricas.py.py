fecha = '\033[m'
amarelo = '\033[0;33m'
vermelho = '\033[0;31m'
azul = '\033[0;34m'
num = int(input('Digite um numero decimal para a CONVERSÃO: '))
conv = str(input(f'Escolha a base:\n{amarelo}1{fecha} para {amarelo}Binario{fecha}\n'
                 f'{azul}2{fecha} para {azul}Octal{fecha}\n'
                 f'{vermelho}3{fecha} para {vermelho}Hexadecimal{fecha}\n'
                 f': ')).strip()
if conv != '1' and conv != '2' and conv != '3':
    print('\nReinicie o programa e escolha o numero certo para a conversão.')

else:
    if conv == '1':
        numbi = bin(num)[2:]
        print(f'O numero {num} convertido em binario fica: {numbi}')

    elif conv == '2':
        numoc = oct(num)[2:]
        print(f'O numero {num} convertido em base octal é: {numoc}')

    elif conv == '3':
        numhe = hex(num)[2:]
        print(f'O numero {num} convertido em hexadecimal é: {numhe}')

print('\nPrograma Finalizado')