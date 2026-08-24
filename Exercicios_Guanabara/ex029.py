#Forma que eu fiz
velocidade = float(input('Qual e a velocidade atual do carro? '))
permitido = 80
if velocidade > permitido:
    multa = (velocidade - permitido) * 7 
    print(f'Multado!Você  lexeceu o limite de velocidade que de {permitido}km/h ')
    print(f'Você levarar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')


#Forma do curso
'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!Você excedeu o limite de velocidade  que é de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com cuidado!')
'''
