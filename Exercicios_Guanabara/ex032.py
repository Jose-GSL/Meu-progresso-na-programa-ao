from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year

res1 = ano  % 4 
res2 = ano % 100
res3 = ano % 400

if (res1 == 0 and res2 != 0) or res3 == 0:
    print(f'O ano {ano} e um ano bisexto')
else:
    print(f'O ano {ano} nao e um ano bisexto')