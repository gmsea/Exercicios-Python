n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
lista = [n1, n2, n3]
numeromaior = lista[0]
numeromenor = lista[-1]

for numero in lista:
    if numero > numeromaior:
        numeromaior = numero

print(f'O maior numero da lista é {numeromaior}')


for numero in lista:
    if numero < numeromenor:
        numeromenor = numero

print(f'E o menor numero na lista é {numeromenor}')