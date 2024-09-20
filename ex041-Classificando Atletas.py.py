from datetime import datetime
ano = datetime.now().year
nas = int(input('Informe o ano de nascimento do atleta: '))
cat = ano - nas
if cat <= 9:
    print('Categoria MIRIM')
if cat > 9 and cat <= 14:
    print('Categoria INFANTIL')
if cat > 14 and cat <= 19:
    print('Categoria JUNIOR')
if cat > 19 and cat <= 20:
    print('Categoria SÊNIOR')
if cat > 20:
    print('Categoria MASTER')