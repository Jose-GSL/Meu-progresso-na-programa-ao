'''Detector de Palíndromo'''

frase = str(input('Digite uma frase: ')).upper()

frase_sem = ''.join(frase.split())
frase_invertida = frase_sem[::-1]

print(f'A frase {frase_sem} invertida e {frase_invertida}')

if frase_sem == frase_invertida:
    print('E um termo PALINDROMO')
else:
    print('Essa frase NÃO E UM POLINFDROMO')

