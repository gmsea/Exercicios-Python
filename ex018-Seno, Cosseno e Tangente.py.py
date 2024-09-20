import math
ang = float(input('Digite um angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O angulo {ang}° tem como seno {sen:.3f}°, cosseno {cos:.3f}° e tangente {tan:.3f}°')