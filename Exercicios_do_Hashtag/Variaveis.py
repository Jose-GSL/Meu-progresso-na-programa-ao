'''Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento final da empresa
após subtrair esse bônus.
● Faturamento inicial: 50.000
● Percentual de bônus: 0.10'''
print('exercicio 1')
lucro = 50000
bonus = 0.10
res1 = lucro * bonus
res2 = lucro - res1
print('Faturamento liquido',res2)
print('Bonus total',res1)

'''Exercício 2: Controle de Estoque de E-commerce (Logística)
Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no
estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um
fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final.'''
print('exercicio 2')
estoque = 250
vendidos = 78 
reposiçao = 100
estoque =  estoque - vendidos + reposiçao
print('Quantidade no fim do dia',estoque)


'''Exercício 3: Divisão de Cargas (Logística/Transporte)
Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
última viagem menor? (Use %)'''

print('EXERCICIO 3')
caixas = 1250
capacidade_caminhoes = 12
caminhoes = caixas // capacidade_caminhoes
resto = caixas % capacidade_caminhoes
print('Caminhões necessarios',caminhoes)
print('Caixas restantes',resto)

'''Exercício 4: Análise de Margem de Lucro (Financeiro)
Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).'''
print('EXERCICIO 4')

faturamento = 15000
custo = 5000
pors_imposto = 0.15

imposto= faturamento * pors_imposto
lucro = faturamento - custo - imposto
margem = lucro / faturamento
margem_atingida = margem > 0.3
print('Meta antigidade?',margem_atingida)

'''Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente
quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de
divisão inteira e resto da divisão para converter os 40 meses.'''
print('EXERCICIO 5')
duraçao = 40
anos = 40 // 12 
meses= 40 % 12 
print(f'{anos} anos e {meses} meses')