'''Próximo Desafio (Mundo 1): Jogo da Adivinhação com Cores ANSI
Para fechar os detalhes do Mundo 1 com chave de ouro, vamos praticar 
Cores no Terminal (códigos ANSI) , Módulorandom e Condicionais .

No Mundo 1, o Guanabara ensina a colocar cores no terminal usando o 
padrão \033[style;text;backgroundm.

Tabela rápida de cores ANSI:
Redefinir (limpar cor):\033[m

Vermelho: \033[31m
Verde: \033[32m
Amarelo: \033[33m
Azul: \033[34m
Roxo: \033[35m
Ciano: \033[36m
Negrito (Negrito): \033[1m

Requisitos do Código:
O computador "Pensa":

O programa deve classificar um número inteiro entre 1 e 5 usando 
random.randint(1, 5).
O Jogador Tenta Adivinhar:

Mostre um título estilizado no terminal (ex: -=-repetir 15 vezes 
em amarelo ou ciano).
Peça para o jogador adivinhar qual número o computador escolheu.
Verificação ( if/ else) com Núcleos:
Se o jogador acertar: Exiba uma mensagem de parabéns em VERDE e 
em NEGRITO .
Se o jogador errar: Exiba uma mensagem informando que ele perdeu 
em VERMELHO , mostrando qual era o número correto que o computador 
tinha pensado.'''

import random 
import time

print('\033[36m-=-' * 18)
print('VOU PENSAR EM UM NÚMERO ENTRE 1 E 5. TENTE ADIVINHAR!')
print('\033[36m-=-\033[m' * 18)

computador = random.randint(0,5)
jogar = int(input('Em que numero eu pensei? '))

print('\033[1;33mPROCESSANDO...\033[m')
time.sleep(0.5)

if computador == jogar:
    print('\033[1;32mGANHOU! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[1;31mGANHEI! Eu pensei no número {computador} e não no {jogar}!\033[m')