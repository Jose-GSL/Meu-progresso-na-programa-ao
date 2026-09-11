'''Desafio: O Oráculo do Aventureiro
Crie um programa em Python que simule um oráculo místico lendo o destino de um novo herói.
Seu código deve cumprir exatamente os seguintes requisitos:

Entrada de dados: Solicite ao usuário que 
digite seu nome completo e sua idade .

Manipulação de Strings 1: Mostre o nome digitado 
todo em guardas e depois tudo em minúsculas .

Manipulação de Strings 2: Calcule e exiba quantas 
letras têm o nome completo (atenção: não conte os espaços em branco!).

Manipulação de Strings 3: Isole e exiba apenas o 
primeiro nome da pessoa e diga quantas letras tem apenas esse primeiro nome.

Módulos: Faça o programa "sortear" um Nível de Sorte 
para o herói, gerando um número inteiro aleatório entre 1 e 100.

Condições ( if/ else):
Se o nível de classificação for maior ou igual a 50 , 
imprima uma mensagem positiva (ex: "Os deuses sorriem para você! Sua jornada será gloriosa." ).
Se for menor que 50 , imprima um alerta (ex: "Cuidado! 
Sua sorte está baixa, você precisa de muito treinamento." )'''

import random 

nome = str(input('Qual e o seu nome? '))
idade = int(input('Quantos anos você tem? '))
separacao = nome.split()

print(f'Seu nome em maiusculo seria: {nome.upper()}')
print(f'Em minusculo ficaria: {nome.lower()}')
print(f'Seu nome tem {len(nome.replace(' ',''))} letras')
print(f'Seu primeiro nome {separacao[0]} e tem {len(separacao[0])} letras')

numero_sorte = random.randint(1,100)
print(f'Seu numero da sorte e {numero_sorte}')

if numero_sorte >= 50:
    print('Os deuses sorriem para você! Sua jornada será gloriosa.')
else:
    print('Cuidado! Sua sorte está baixa, você precisa de muito treinamento.')



