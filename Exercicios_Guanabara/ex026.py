frase = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra A aparace {frase.count('a')} ')
print(f'A letra A aparece pela primeira vaz na posição {frase.find('a') + 1}')
print(f'A ultima letra A apareceu na posição {frase.rfind('a') + 1}')