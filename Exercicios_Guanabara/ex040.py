'''Aquele classico da Média'''

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2
print(f'Sua media e de {media:.1f}')

if media >= 7:
    print('Você esta APROVADO')
elif media == 5 and media < 7:
    print('Você esta em RECUPERÇÃO')
elif media < 5:
    print('Você foi REPROVADO')