'''Maior e menor da sequência'''

pesos = []

for p in range(1,6):
    p = float(input(f'Peso da {p}º pessoa: '))
    pesos.append(p)

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'O maior peso lido foi de {maior_peso}Kg')
print(f'O menor peso lido foi de {menor_peso}Kg')