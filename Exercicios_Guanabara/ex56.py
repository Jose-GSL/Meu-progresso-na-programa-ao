'''Analisador completo'''

nome_velho = ''
maioridadehomen = 0
mulheres = 0
somaidade = 0
mediaidade = 0


for p in range(1,5): 
    print(f'------ {p}º PESSOA ------')
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

mediaidade = somaidade / 4 
print(f'A media de idade do grupo e de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomen} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos')