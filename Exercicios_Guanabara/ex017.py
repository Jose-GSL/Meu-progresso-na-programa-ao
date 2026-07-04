import math
co = float(input('Digite o cateto osposto:'))
ca = float(input('Digite o cateto adjacente:'))
hi = math.hypot(co, ca)
#hi = (co ** 2 + ca ** 2) ** 0.5
print(f'A hipotenusa vai medir {hi:.2f}')
