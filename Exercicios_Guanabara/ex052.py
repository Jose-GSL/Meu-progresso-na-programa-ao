'''Números primos'''

numero = int(input('Digite um numero inteiro: '))

divisivel = 0

for num in range(1,numero + 1):
    if numero % num == 0:
        divisivel += 1
        print('\033[33m ',end='')
    else:
        print('\033[31m ',end='')
    print(f'{num} \033[m',end='')

print(f'\nO numero {numero} foi divisivel {divisivel} vezes')
if divisivel == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
