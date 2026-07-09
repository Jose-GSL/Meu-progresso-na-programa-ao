numero = int(input('Digite um numero: '))
uni = numero // 1 % 10 #ele pegar o numero e faz uma divisão interira, e depois tira o resto da divisão por 10 
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10

print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')