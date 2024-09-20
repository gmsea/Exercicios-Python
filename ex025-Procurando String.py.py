name = str(input('Digite seu nome completo: ')).strip()
up = name.upper()
find = 'SILVA'
if find in up:
    print('Esse nome tem Silva')
else:
    print('Essa nome nao tem Silva')
