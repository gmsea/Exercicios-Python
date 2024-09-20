dias = int(input('Quantos dias o carro foi alugado? '))
kms = float(input('Quantos kilometros foi utilizado o carro? '))
valor = (dias * 60) + (kms * 0.15)
print(f'O valor total dos da locação fica em R${valor:.2f}')
