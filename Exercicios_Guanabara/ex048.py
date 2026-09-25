'''Soma impares multiplos de tres'''
cont = 0
soma = 0 
for n in range(1,501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n
print(f'A soma de todos os {cont} valores solicitados e de {soma}')
print('fim') 