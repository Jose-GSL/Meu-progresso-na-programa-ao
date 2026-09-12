'''Próximo Desafio (Mundo 1): O Reajuste do Planeta Bissexto

Neste exercício você vai praticar condições compostas ( and/ or), 
o operador resto da divisão ( %), fatiamento de strings e 
formatação matemática .

Requisitos do Código:
Entrada de dados:

Carga do funcionário (ex: "Engenheiro", "Piloto").

Salário atual (ex: 2500.00).

Ano de contratação (ex: 2024).

Manipulação de String:

Pegue a carga digitada, remova os espaços e mostre uma tag de 3 
letras em maiúsculo usando fatiamento (ex: "Engenheiro"vira ENG).

Condicionais com Reajuste Salarial ( if/ else):

Se o salário for maior que R$ 3.000,00 , o aumento será de 10% .

Se for menor ou igual a R$ 3.000,00 , o aumento será de 15% .

Mostre o valor do aumento e o novo salário final.

Condição Matemática (Ano Bissexto):

Verifique se o ano de contratação é um ano bissexto .

Regra do Ano Bissexto: O ano deve ser divisível por 4 ( ano % 4 == 0), 
E NÃO pode ser divisível por 100 ( ano % 100 != 0), A MENOS QUE seja 
divisível por 400 ( ano % 400 == 0).

Exiba se a contratação ocorreu em ano bissexto ou não.'''

import calendar


cargo = str(input('Cargo na empresa: ')).upper()
salario = float(input('Salrio atual: '))
ano = int(input('Ano de contratação: '))
print(f'Cargo: {cargo.capitalize()}')
print(f'Salario Atual: {salario:.2f}')
print(f'Ano de Contratação: {ano}')

print(f'Tag do Cargo: {cargo [0:3]}')
print(f'O ano {ano} e um ano bisxesto? ', calendar.isleap(ano))

if salario > 3000:
    aumento = salario * 10 / 100 
    salario_novo = aumento + salario
    print(f'Aumento aplicado: {aumento:.2f} (10%)')
    print(f'Salario novo: R${salario_novo:.2f}')
else:
    aumento = salario * 15 / 100 
    salario_novo = aumento + salario
    print(f'Aumento aplicado: {aumento:.2f} (15%)')
    print(f'Salario novo: R${salario_novo:.2f}')