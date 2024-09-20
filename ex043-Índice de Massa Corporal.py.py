def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print('-=-' * 10)
print('Calculadora de IMC')
print('-=-' * 10)

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = calcular_imc(peso, altura)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Voce esta abaixo do peso.')
if imc <= 25 and imc >= 18.5:
    print('Voce esta no seu peso ideal')
if imc > 25 and imc < 30:
    print('Voce esta no sobrepeso')
if imc >= 30 and imc <= 40:
    print('Voce esta obeso')
if imc > 40:
    print('Voce Esta em obesidade morbida')