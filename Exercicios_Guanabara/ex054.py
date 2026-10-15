'''Grupo da Maioridade'''

import datetime

ano_atual = datetime.date.today().year
idades = []

print('Digiteo ano de nascimenro de sete pessoas abaixo')


for i in range(1,8):
    i = int(input(f'Em que ano a {i}º pessoa narceu? '))
    idades.append(i)

maiores_idade = 0
menor_idade = 0

for idade in idades:
    if ano_atual - idade >= 18:
        maiores_idade += 1
    elif ano_atual - idade < 18:
        menor_idade += 1 
print(f'Ao todo temos {maiores_idade} maiores de idade')
print(f'E tambem tivemos {menor_idade} menores de idades')