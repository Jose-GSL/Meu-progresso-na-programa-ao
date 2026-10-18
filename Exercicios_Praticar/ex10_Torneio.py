'''Desafio Final do for: O Torneio de Programação Intergaláctico
Para fechar o laço forcom chave de ouro antes de irmos 
para a estrutura while, este desafio vai exigir um controle 
completo de estatísticas e validação de texto.

Requisitos do Código:
Laço de Repetição ( for):

O torneio terá 5 participantes . Chore um forde 1 a 5.

Entrada e Tratamento de Dados (Mundo 1):
Nome do competidor:  .strip()e .title().
Linguagem escolhida: O usuário digital 'PYTHON', 'JAVA'ou 
'C++'. Converta para guardas com .upper().
Pontuação na prova: Número inteiro ( int).

Pontuação Bônus e Classificação (Mundo 2):
A pontuação base é aquela que foi digitalizada.
Bônus Python: Se a linguagem for 'PYTHON', o participante ganha 
+10 pontos bônus na pontuação final.
ovino:
Pontuação final maior ou igual a 80 :[CLASSIFICADO PARA A FINAL]
Pontuação final entre 50 e 79 :[EM ANÁLISE]
Pontuação final menor que 50 :[DESCLASSIFICADO]

Gerador de Hash da Inscrição (Mundo 1):
Monte uma string com:
A última letra do nome em guardas + #+ número do competidor no 
loop+ -+ número aleatório entre 10 e 99( random).
Exemplo para a 1ª pessoa "Lucas":  S#1-42.

Relatório Final (Fora do for):
Média de pontuação de todos os concorrentes.
Total de classificados para a final .
Total de desenvolvedores que obtiveram PYTHON .
Nome , linguagem e pontuação do CAMPEÃO (maior pontuação).'''

import random

campeão = ''
lin_campeão = ''
pontos_cam = 0

soma_pontuação = 0
classificados = 0
dev_python = 0


print('=== TORNEIO INTERGALÁCTICO DE CÓDIGO ===')

for c in range(1,6):
    print(f'----- {c}º COMPETIDOR -----')
    nome = str(input('Nome: ')).strip().title()
    linguagem = str(input('Linguagem [PYTHON / JAVA / C++]: ')).strip().upper()
    pontuação = int(input('Pontuação Base: '))

    hash = f'{nome[-1]}#{c}-{random.randint(10,99)}'
    print(f'[Hash: {hash}]')

    if linguagem == 'PYTHON':
        pontuação += 10
        dev_python += 1

    if pontuação >= 80:
        print('[CLASSIFICADO PARA A FINAL]')
        classificados += 1
    elif  pontuação >= 50:
        print('[EM ANALISE]')
    else:
        print('[DESCLASSIFICADO]')

    if c == 1 or pontuação > pontos_cam:
        campeão = nome
        lin_campeão = linguagem
        pontos_cam = pontuação

    soma_pontuação += pontuação

media = soma_pontuação / 5

print(f'{"==" * 5} RELATÓRIO DO TORNEIO {"==" * 5}')
print(f'- Média das pontuações: {media:.1f}')
print(f'- Total de Classificados: {classificados}')
print(f'- Desenvolvedores Python: {dev_python}')
print(f'- Campeão: {campeão} com {pontos_cam} pontos (Linguagem: {lin_campeão})')

