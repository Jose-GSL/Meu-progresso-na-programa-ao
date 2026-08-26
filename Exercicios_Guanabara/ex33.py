print('Digite os valores a abaixo')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

maior = a 
menor = a 

if b<a and b<c:
    menor = b
if c<a and c<a:
    menor = c 

if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O menor numero digitado foi {menor}')
print(f'O maior numero digitado foi {maior}')