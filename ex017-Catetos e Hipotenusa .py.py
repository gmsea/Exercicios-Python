import math
op = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))
hip = math.hypot(op, adj)
print(f'A Hipotenusa valer {hip}')