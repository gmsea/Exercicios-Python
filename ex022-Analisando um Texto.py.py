nome = str(' Gabriel Matos Seabra ')
n1 = nome.upper()
n2 = nome.lower()
n3 = len(nome.replace(' ', ''))
n4 = nome.split()
n5 = len(n4[0])
print(f'O nome é: {nome}')
print(f'Nome em maiúsculas: {n1}')
print(f'Nome em minúsculas: {n2}')
print(f'Número de letras (sem espaços): {n3}')
print(f'Quantidade de letras do primeiro nome: {n5}')