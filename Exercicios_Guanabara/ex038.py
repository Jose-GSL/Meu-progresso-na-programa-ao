'''Comparado Numeros'''

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))

if num1 > num2:
    print('O primeiro numero é maior')
elif num2 > num1:
    print('O segundo numero e maior')
else:
    print('Não existe maior, os dois são iguais')