print('-=-'*10)
print('-=Analizador de Triangulos=-')
print('-=-'*10)
a = int(input('Digite o tamanho da primeira reta: '))
b = int(input('Digite o tamanho da segunda reta: '))
c = int(input('Digite o tamanho da terceira reta: '))
if (a + b > c) and (a + c > b) and ( b + c > a):
    print('As retas escolhidas podem formar um triangulo')
else:
    print('As retas escolhidas não podem formar um triangulo')