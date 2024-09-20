nome = str(input('Digite seu nome: ')).strip().upper()
n1 = nome.split()
first = n1[0]
last = n1[-1]
print(f'O primeiro nome é {first}')
print(f'O ultimo nome é {last}')
