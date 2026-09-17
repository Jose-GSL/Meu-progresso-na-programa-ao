'''Gernciamneto de Pagamento'''

preço = float(input('Digite o preço do protudo: R$'))

lista_pagamento = ['A vista','A vista no cartão','Em ate 2x no carta','Ou 3x vezes ou mais no cartão']

print('Formas de pagamentos')
print(lista_pagamento[0])
print(lista_pagamento[1])
print(lista_pagamento[2])
print(lista_pagamento[3])

lista1 = [texto.lower() for texto in lista_pagamento] #tranforma o textos da lista de pagamento em minusculo 
forma = str(input('Digite a forma de pagamento: ')).lower().strip()

if forma == lista1[0]:
    desconto = preço - (preço * 10 / 100)
    print(f'A pagara R${desconto:.2f} reais pelo protudo')
elif forma == lista1[1]:
    desconto = preço - (preço * 10 / 100)
    print(f'A pagara R${desconto:.2f} reais pelo protudo')
elif forma == lista1[2]:
    por_mes = preço / 2 
    print(f'Você pagara R${por_mes:.2f} por mes')
elif forma == lista1[3]:
    parcela = int(input('Em quantas vezes vc quer parecelar: '))
    juros = preço + (preço * 20 / 100)
    por_mes = juros / parcela
    print(f'você pagara R${por_mes:.2f} por mes')