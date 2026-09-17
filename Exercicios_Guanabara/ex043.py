'''Indice de Massa comrporal'''

altura = float(input('Digite sua altura: (m)'))
peso = float(input('Digite seu peso: (Kg)'))

imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
print('Você esta ', end = ' ')

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <=  25:
    print('com o PESO normal.PARABENS!')
elif imc <= 30:
    print('em SOBREPESO')
elif imc <=  40: 
    print('em OBESIDADE')
else:
    print('em OBESIDADE MÓRBIDA.CUIDADO!')
