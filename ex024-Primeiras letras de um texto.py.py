city = str(input('Digite a cidade que voce nasce: ')).strip()
up = city.upper()
div = up.split()
prim = div[0]
if prim == 'SANTO':
    print('Essa cidade começa com Santo')
else:
    print(f'Essa cidade nao começa com Santo começa com {prim}')
