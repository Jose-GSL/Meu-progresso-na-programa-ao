'''Desafio: O Inspetor de Qualidade de Drones
Você foi contratado por uma empresa de logística para programar o 
sistema de testes automáticos de um lote de drones de entrega. O 
programa deve processar exatamente 4 drones em um laço for.

Requisitos do Código:
Laço de Repetição ( for):
Crie um laço forde 1 a 4 para funcionar cada um dos 4 drones.

Entrada e Tratamento de Dados (Mundo 1):
Modelo do drone: Limpe os espaços nas pontas com .strip()e transforme 
tudo em guardas com .upper().
Nível de bateria (%): Valor inteiro ( int).
Peso da carga transportada (kg): Valor decimal ( float).

Gerador de Código de Inspeção (Mundo 1):
Para cada drone, monte uma tag única combinando:
As 3 primeiras letras do modelo do drone + #+ número da pessoa/drone no 
loop+ -+ um número aleatório entre 100 e 999(usando random.randint).
Exemplo para o 1º drone "SKYHAWK": SKY#1-842 .

Classificação do Status ( if / elif / else- Mundo 2):
Se a Bateria for menor que 20%: O status será [RECUSADO: BATERIA CRÍTICA]
(independente do peso).
Se a Bateria for maior ou igual a 20%:
Se o peso para até 15,0 kg : Status [APROVADO: CARGA LEVE/MÉDIA].
Se o peso for maior que 15,0 kg : Status [APROVADO: CARGA PESADA].

Estatísticas e Relatório Final (Mundo 2):
Ao final das 4 inspeções (fora do for), exiba:
Média do peso de todas as cargas testadas.
Total de drones APROVADOS (soma dos leves e pesados) e total de RECUSADOS .
O modelo e a bateria do drone que carregou o peso MAIOR .'''


import random

media_peso = 0
soma_peso = 0
drones_aprovados = 0
drones_recusado = 0

maior_peso = 0
modelo_maior_peso = ''
bateria_maior_peso = 0

print('=== INSPEÇÃO DE DRONES DE CARGA ===')

for d in range(1,5):
    print(f'----- {d}º DRONE -----')
    modelo = str(input('Modelo: ')).strip().upper()
    bateria = int(input('Bateria (%): '))
    peso = float(input('Peso da carga (kg): '))
    soma_peso += peso

    codigo = f'{modelo[0:3]}#{d}-{random.randint(100, 999)}'
    print(f'[Codigo: {codigo}]')
    print('Status: ', end=' ')

    if bateria < 20:
        drones_recusado += 1
        print('[RECUSADO: BATERIA CRÍTICA]')
    elif bateria >= 20 and peso <= 15:
        drones_aprovados += 1
        print('[APROVADO: CARGA LEVE/MÉDIA]')
    else:
        drones_aprovados += 1 
        print('[APROVADO: CARGA PESADA]')

    if d == 1 or peso > maior_peso:
        maior_peso = peso
        modelo_maior_peso = modelo
        bateria_maior_peso = bateria 

print(f'{"==" * 5} RELATÓRIO TÉCNICO {"=="* 5}')
media_peso = soma_peso / 4
print(f'- Média do peso transportado: {media_peso} kg')
print(f'- Drones Aprovados: {drones_aprovados} | Drones Recusados: {drones_recusado}')
print(f'-Drone com maior carga: {modelo_maior_peso} ({maior_peso}) com {bateria_maior_peso} de bateria.')
