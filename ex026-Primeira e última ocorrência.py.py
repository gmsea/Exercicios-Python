name = str(input('Escreva uma frase: ')).strip()
up = name.upper()
count = up.count('A')
first = int(up.find('A')) + 1
second = int(up.rfind('A')) + 1
print(f'A letra a apareceu na frase {count} vezes')
print(f'A letra a apareceu pela primeira vez na posição {first} ')
print(f'A letra a apareceu pela segunda vez na posição {second} ')