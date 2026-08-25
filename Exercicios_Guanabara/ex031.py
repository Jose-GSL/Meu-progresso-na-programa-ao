distancia = float(input('Digite a distancia da  sua viagem em km: '))
print(f'Você esta preste a começar uma viagem de {distancia:.1f}km.')

if distancia <= 200:
    cobrar = distancia * 0.50
    print(f'E o preço de sua passagem sera de R${cobrar:.2f} ')
else:
    cobrar = distancia * 0.45
    print(f'E o preço de sua passagem sera de R${cobrar:.2f}')
