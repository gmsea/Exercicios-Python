clo = '\033[m'
yel = '\033[0;33m'
red = '\033[0;31m'
blu = '\033[0;34m'
gre = '\033[0;32m'
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print(f'Sua média foi de {media:.1f} e voce ficou {red}REPROVADO{clo} por {media - 5.0:.1f} pontos')
if media >= 5.0 and media < 7.0:
    print(f'Sua média foi de {media:.1f} e voce ficou de {blu}RECUPERAÇÃO{clo} por {media - 7.0:.1f} pontos')
if media >= 7.0:
    print(f'Sua média foi de {media:.1f} e voce foi {gre}APROVADO{clo} ')

print('\nObrigado pela consulta!')