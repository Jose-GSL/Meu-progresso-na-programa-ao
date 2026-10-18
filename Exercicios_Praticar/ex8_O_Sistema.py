'''Desafio: O Sistema de Controle do Cinema Espacial
Você foi contratado para programar o terminal de vendas 
de ingressos para a grande estreia no Cinema Espacial . 
O programa deve processar as compras de exatamente 5 
clientes em um laço for.

Requisitos do Código:
Laço de Repetição ( for):
Crie um laço forde 1 a 5 para cadastrar os 5 clientes.

Entrada e Manipulação de Dados (Mundo 1):
Nome do cliente: Remova espaços nas pontas ( .strip()) 
e deixe apenas a primeira letra em guardas ( .capitalize()).
Idade: Número inteiro ( int).
Poltrona escolhida: O usuário digital o setor ( 'VIP', 
'MEZANINO'ou 'PISTA'). Converta para guardas ( .upper()).

Cálculo do Ingresso ( if / elif / else- Mundo 2):
O preço base do ingresso é R$ 40,00 .
Se o setor for 'VIP': acréscimo de 50% (R$ 60,00).
Se o setor for 'MEZANINO': acréscimo de 20% (R$ 48,00).
Se o setor for 'PISTA': mantém R$ 40,00.

Bônus Estudante/Menor (Mundo 1): Se a idade for menor que 
18 anos , aplique um desconto de 50% sobre o valor final 
da poltrona calculada.

Gerador de Ticket de Embarque (Mundo 1):
Monte um código único para o ingresso combinado:
As 3 primeiras letras do nome em guardas + -+ número da 
pessoa no loop+ #+ um número aleatório entre 10 e 99(usando
random.randint).
Exemplo para a 1ª pessoa "Gabriel": GAB-1#47 .

Relatório Final (Acumuladores do Mundo 2):
Ao final das 5 compras (fora do for), exiba:
Total arrecadado com todas as vendas (soma dos ingressos).
Total de ingressos VIP vendidos.
Média de idade dos clientes.
O nome e o valor pago do cliente que fez a compra mais cara .'''

import random

nome_mais_caro = ''
maior_valor = 0 
arregadado = 0
pagar = 0
somaidade = 0
mediaidade = 0 

vipvendido = 0

print('=== CINEMA ESPACIAL - VENDA DE INGRESSOS ===')

for c in range(1,6):
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    somaidade += idade 
    poltrona = str(input('Poltrona [VIP / MEZANINO / PISTA]: ')).upper()

    ticket = f'{nome[0:3]}-{c}#{random.randint(10,99)}'
    print(f'[Ticket Gerado: {ticket}]')


    if poltrona == 'VIP':
        pagar = 60
        vipvendido += 1 
    elif poltrona == 'MEZANINO':
        pagar = 48
    else:
        pagar = 40

    if idade < 18:
        pagar /= 2
    arregadado += pagar
    print(f'Valor a pagar: R$ {pagar:.2f}')


    if c == 1 or pagar > maior_valor:
        maior_valor = pagar
        nome_mais_caro = nome

mediaidade = somaidade / 5
print(f'{"==" * 5 } RELATÓRIO DE VENDAS {"=="* 5}')

print(f'- Arrecadação Total: R$ {arregadado:.2f}')
print(f'- Ingressos VIP vendidos: {vipvendido}')
print(f'- Média de idade dos clientes: {mediaidade} anos')
print(f'- Maior compra: {nome_mais_caro} pagou R$ {maior_valor}')


