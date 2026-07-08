nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome em maiusculo fica {nome.upper()}')
print(f'Seu nome em minusculo fica {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(' ')}')

separa = nome.split()
print(f'seu primeiro nome {separa[0]} tem {nome.find(' ')} letras')