'''Próximo Desafio (Mundo 1): O Testador de Escudos Espaciais
Neste desafio você vai praticar Geometria Básica,
Condições de Existência, Módulo random e Formatação no Terminal.Requisitos do Código:Entrada de Dados:Peça o 
tamanho de 3 hastes de metal que compõem a estrutura do escudo (h1, h2, h3 em float).Lógica de Existência de 
Triângulos (if/else):Três segmentos só formam um triângulo se a soma de dois lados for maior que o terceiro 
lado (para todas as combinações):$h1 + h2 > h3$ e $h1 + h3 > h2$ e $h2 + h3 > h1$Módulo random e 
Cálculos:Se formar um triângulo válido:Calcule o Perímetro da estrutura ($h1 + h2 + h3$).Sorteie a cor do campo 
de força usando random.choice(['Azul', 'Verde', 'Dourado']).Exiba a mensagem de aprovação com o perímetro e a cor sorteada.
Se NÃO formar um triângulo:Exiba a mensagem de alerta informando que a estrutura é incompatível e vai colapsar.'''

import random

h1 = float(input('Comprimento da Haste 1: '))
h2 = float(input('Comprimento da Haste 2: '))
h3 = float(input('Comprimento da Haste 3: '))

print(f'Analisando hastes: {h1},{h2},{h3}...')

if h1 + h2 > h3 and h1 + h3 > h2 and h2 + h3 > h1:
    cor = random.choice(['Azul', 'Verde', 'Dourado'])
    perimetro = h1 + h2 + h3

    print('[SUCESSO] As hastes conseguem formar um triângulo estrutural!')
    print(f'Cor do escudo ativado: {cor}')
    print(f'Perímetro total:{perimetro:.1f} unidades')
else:
    print('[FRACASSO] As hastes não conseguem formar um triângulo estrutural!')

















