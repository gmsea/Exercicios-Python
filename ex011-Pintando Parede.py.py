alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = alt * lar
tinta = area / 2
print(f'A area da parede é de {area:.2f}m² e sera necessario {tinta:.1f} litros de tinta para pinta-la')