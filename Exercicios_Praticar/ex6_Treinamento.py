'''Desafio: O Centro de Treinamento de Astronautas
Você foi encarregado de criar o sistema de triagem 
da Agência Espacial. O programa deve realizar uma 
contagem regressiva de inicialização, cadastrar uma 
equipe de candidatos e gerar um relatório estatístico 
completo.

Requisitos do Código:
Contagem Regressiva ( for+ time.sleep):

Antes de iniciar os cadastros, faça uma partição de 
inicialização do sistema de 3 a 1 usando um laço forcom 
range(), com intervalo de 0,5 segundo entre cada número 
(módulo time).

Cadastro em Loop ( for):

O sistema deve cadastrar exatamente 4 candidatos. 
Use um laço forpara repetir a leitura dos dados 4 vezes:
Nome do candidato (trate a string com .strip()).
Idade ( int).
Horas de voo simulado ( float).

Classificação de Categoria ( if/ elif/ else):

Para cada candidato cadastrado, exiba imediatamente a sua 
patente com base nas horas de voo:

Menos de 50 horas: [NOVATO]
De 50 a 150 horas: [VETERANO]
Mais de 150 horas: [COMANDANTE]

Análise de Dados do Grupo (Acumuladores e Variáveis ​​de
Controle):

Ao final do laço de reprodução, o programa deve exibir 
um relatório geral contendo:

A média de idade do grupo.
O nome e a idade do candidato mais velho.
A quantidade total de candidatos que alcançaram o nível 
de Comandante (mais de 150h).'''


import time 

print('=== INICIALIZANDO O SISTEMA ESPACIAL ===')
for a in range(3, 0, -1):
    print(a,'...')
    time.sleep(0.5)
print('SISTEMA PRONTO!')

idades = []
nomes = []
horas = []
numeros = [1,2,3,4]

soma_idade = 0
total_comandantes = 0

for n in range(1,5):
    print(n,'º Pessoa')
    n = str(input('Digite seu nome:')).capitalize()
    nomes.append(n)

    i = int(input('Digite sua idade: '))
    idades.append(i)
    soma_idade += i
    h = int(input('Digite suas horas de voo(ex:50): '))
    horas.append(h)

for nome, idade, hora, numero in zip(nomes,idades,horas,numeros):
    print(f'{'==' * 5} {numero}º pessoa {'==' * 5}')
    print('Nome:', nome)
    print('Idade: ',idade)
    print('horasde voo: ', hora)
    if hora < 50:
        print('[NOVATO]')
    elif hora >= 50 and hora <= 150:
        print('[VETERANO]')
    else:
        total_comandantes += 1
        print('[COMANDANTE]')

maior_idade = max(idades)
posiçao = idades.index(maior_idade)
nome_velho = nomes[posiçao]

print(f'{'==' * 5} RELATORIO FINAL {'==' * 5}')
print('- Média de idade do grupo:', soma_idade / 4)
print(f'- O candidato mais velho é {nome_velho} com {maior_idade} anos.')
print(f'- Total de Comandantes cadastrados: {total_comandantes}')