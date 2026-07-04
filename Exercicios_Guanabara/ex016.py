import math
numero = float(input('Digite um valor:'))
print(f'O numero {numero} tem a parte inteira {round(numero)}')#Tranforma o numero em inteiro dependo da distancia de do numero
print(f'O numero {numero} tem a parte inteira {math.ceil(numero)}')#transforma em inteiro  como 6.18 vira 7, Tranformando em interiro em um numero acima 
print(f'O numero {numero} tem a parte inteira {math.floor(numero)}')#Tranforma em interiro de 6.18 par, a 6, so tirando os numero depois do ponto, transformando em
print(f'O numero {numero} tem a parte inteira {math.trunc(numero)}')
print(f'O numero {numero} tem a parte inteira {int(numero)}')