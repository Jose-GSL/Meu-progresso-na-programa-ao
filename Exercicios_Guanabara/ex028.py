'''FORMA QUE EU FIZ'''

import random 
import time
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar ')
numero = int(input('Digite o numero em que esta pensando? '))
time.sleep(2)
print('PROCESSANDO...')

computador = random.randint(0,5)# faz com que o programa escolha um numero entre 0 a 5 
if numero == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no numero {computador} e não no {numero}')
print('--FIM--')

'''FORMA QUE P GUANABARA FEZ'''
'''
from random import randint
from time import sleep

computador2 = randint(0,5)
print('__' * 30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinha ')
print('__' * 30)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESANDO...')
sleep(2)

if jogador == computador2:
    print('PARABÉNS! Você conseguiu vencer')
else:
    print(f'GANHEI! Pensei no numero {computador2} e nao no {jogador}')
'''