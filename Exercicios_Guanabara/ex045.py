'''Jogo de Pedra, Papel e Tesoura'''
import random

print('Vamos jogar JOKENPO')
print('Suas opções são:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

formas = ['PEDRA','PAPEL','TESOURA']
jogador = int(input('Qual e sua jogada? '))
computador = random.randint(0,2)
escolha = formas[jogador]

print('JO\nKEN\nPO!!!')

print('-=-' * 8)
if computador == 0:
    print('Computador escolheu PEDRA')
elif computador == 1:
    print('Computador escolheu PAPEL')
else:
    print('Computador escolheu TESOURA')
print(f'Jogador jogou {escolha}')
print('-=-' * 8)

if jogador == computador:
    print('EMPATAMOS')
elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    print('JOGADOR VENCEU')
else:
    print('COMPUTADOR VENCEU')

