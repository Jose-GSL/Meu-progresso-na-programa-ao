'''Desafio: O Gerenciador do Estreito de Embarcações
Um canal de navegação precisa controlar o fluxo de 
barcos que atravessam uma eclusa. O sistema deve 
funcionar exatamente 6 embarcações numeradas.

Requisitos do Código:

Laço com Intervalo ( forem rangede 2 em 2):
O sistema funciona apenas como cabines pares: crie 
um laço forque vai de 2 até 12, pulando de 2 em 2 
( range(2, 13, 2)).

Entrada e Validação de Dados (Mundo 1):

Nome do capitão: Remova os espaços extras com .strip()
e deixe todas as palavras com a primeira letra designada 
usando .title().
Comprimento da barra (em metros): Valor decimal ( float).

Cálculo da Taxa de Atravessamento ( if / elif / else- Mundo 2):
Barcos de até 10,0 metros : Taxa de R$ 50,00 .
Barcos de 10,1 a 25,0 metros : Taxa de R$ 120,00 .
Barcos de mais de 25,0 metros : Taxa de R$ 250,00 .

Bônus de Nome Longo (Mundo 1): 
Se o nome do capitão tiver mais de 15 caracteres 
(dica: len(nome) > 15), concede um desconto de R$ 20,00 
na taxa final.

Gerador de Registro da Cabine:

Monte uma tag para o recibo contendo:

As 2 primeiras letras do nome do capitão em oficiais + @+ número 
da cabine no loop+ -+ um número aleatório entre 100 e 500(módulo 
random).

Exemplo para a cabine 2 com o capitão "Roberto": RO@2-341 .

Relatório Final (Fora do for):

Ao final das 6 inspeções, exiba:

Total arrecadado com todas as taxas cobradas.

Quantidade de barcos grandes (comprimento maior que 25 metros).

O comprimento do maior barco funcionado e o nome do seu capitão .'''

import random 

taxa = 0
arregadado = 0
barcos_grandes = 0

maior_barco = 0
capitão_maiorbarco = ''

print('=== CONTROLE DE FLUVO DO ESTREITO ===')
for c in range(2, 13, 2 ):
    nome = str(input('Nome do Capitão: ')).strip().title()
    barco = float(input('Comprimento do barco (m): '))

    registro = f'{nome[0:2].upper()}#{c}-{random.randint(100,500)}'
    print(f'[Registro: {registro}]')

    if barco <= 10:
        taxa = 50
    elif barco <= 25:
        taxa = 120
    else:
        barcos_grandes += 1 
        taxa = 250

    if len(nome) > 15:
        taxa -= 20
        print(f'Taxa cobrada: R$ {taxa:.2f}(Desconto de nome longo aplicado!)')
    else:
        print(f'Taxa cobrada: R$ {taxa:.2f}')
    arregadado += taxa 

    if c == 2 or barco > maior_barco:
        maior_barco = barco
        capitão_maiorbarco = nome 

print(f'{"==" * 5} RELATÓRIO DO DIA {"==" * 5}')
print(f'- Arrecadação Total: R$ {arregadado:.2f}')
print(f'- Embarcações grandes (> 25m): {barcos_grandes}')
print(f'- Maior embarcação: {maior_barco:.1f} (Capitão: {capitão_maiorbarco})')