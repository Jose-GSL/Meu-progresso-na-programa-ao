'''Emprestimo bancario'''

casa = float(input('Digite o valo da casa: R$'))
salario = float(input('Salario do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))

pretaçao = casa / (ano * 12)
limite = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {ano} a pretação será de R${pretaçao:.2f}')

if limite >= pretaçao:
    print('\033[32mEMPRESTIMO APROVADO!\033[m')
else:
    print('\033[31mEMPRESTIMO NEGADO!\033[m')