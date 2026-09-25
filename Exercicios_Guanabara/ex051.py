'''Prograsssão Aritmetica'''

termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razão

for pa in range(termo, decimo + razão, razão):
    print(f'{pa} ->',end=(' '))
print('acabou', end=(' '))
