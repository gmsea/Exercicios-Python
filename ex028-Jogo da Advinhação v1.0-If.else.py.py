import random
import time

num = random.randint(1,5)
cho = int(input('Tente acerta o numero que eu escolhi: '))
print('Processando...')
time.sleep(1)
if cho == num:
    print('Parabens vem acertou !')
else:
    print('Ahh voce errou !')
print(f'Meu Numero escolhido foi {num}.')
