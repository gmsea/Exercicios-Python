ano = int(input('Digite um ano: '))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'Voce acertou, o ano {ano} é bissexto')
else:
    print(f'Voce errou, o ano {ano} não é bissesto')