velocidade = int(input('Qual e a velocidade atual do carro? '))
permitido = 80
if velocidade == permitido:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (velocidade - 80) * 7 
    print(f'O limite de velocidade e {permitido}km/h ')
    print('Você levarar uma multa de R${multa}')


