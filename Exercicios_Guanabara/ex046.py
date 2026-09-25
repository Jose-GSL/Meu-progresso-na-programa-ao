'''Contagem regressiva'''
import time

print('Os fogos de Artificio estorara em...')
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('BUM! BUM! POOM!')