import random 

total_multa = 0
multados = 0
soma_velo = 0
placa_rapida = ""
maior_velo = 0

for v in range(1,5):
    print(f'----- {v}º VEÍCULO -----')
    placa = str(input('Placa: ')).strip().upper()
    tipo = str(input('Tipo [CARRO / MOTO / CAMINHAO]: ')).lower().strip()
    velocidade = float(input('Velocidade (km/h): '))
    soma_velo += velocidade

    if v == 1 or velocidade > maior_velo:
        placa_rapida = placa
        maior_velo = velocidade

    protocolo = f'{placa[:3]}-{v}#{random.randint(100,999)}'
    print(f'Protocolo: {protocolo}')

    print('status:', end= '')
    if velocidade <= 80:
        print('[DENTRO DO LIMITE - SEM MULTA]')

    elif tipo in ('carro','moto'):
        exesso = velocidade - 80
        multa = exesso * 7 
        total_multa += multa
        multados += 1
        print(f'MULTADO! Valor da multa: R$ {multa:.2f}')

    elif tipo == 'caminhao':
        exesso = velocidade - 80
        multa = exesso * 15
        total_multa += multa
        multados += 1
        print(f'MULTADO! Valor da multa: R$ {multa:.2f}')
    print(' ')
    
media = soma_velo / 4

print('================ RELATÓRIO DO RADAR ================')
print(f'- Arrecadação Total em Multas: R$ {total_multa:.2f}')
print(f'- Total de Veículos Multados: {multados}')
print(f'- Média de Velocidade: {media:.1f} km/h')
print(f'- Veículo mais rápido: {placa_rapida} a {maior_velo} km/h')





