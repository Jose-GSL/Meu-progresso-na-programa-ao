'''Conversor de Bases Numericas'''
num = int(input('Digite um numero inteiro: '))
print('[ 1 ] para BiNARIO')
print('[ 2 ] para OCTAL')
print('[ 3 ] para HEXADECIMAL')

escolha = int(input('Sua opção: '))

binario = bin(num)[2:]
octal = oct(num)[2:]
hexad = hex(num)[2:]

if escolha == 1:
    print(f'{num} convertido para BINARIO é igual a {binario}') #outra forma de usar seria trocar 'BIANRIO' do .format para o proprio codigo como bin(num)[2:] funciona 
elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a {octal}')
else:
    print(f'{num} convertido para HEXADECIMAL é igual a {hexad}') 