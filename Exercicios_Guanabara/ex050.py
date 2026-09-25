'''Soma dos pares'''

print('Digte seis valore abaixo')
soma = 0
cont = 0

for c in range(1,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        cont += 1
        soma += n
print(f'Você informou {cont} numeros pares- e a soma foi {soma}')