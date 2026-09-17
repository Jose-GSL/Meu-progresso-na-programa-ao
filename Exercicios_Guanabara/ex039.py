'''Alistamento Militar '''
import datetime

nas = int(input('Digite seu ano de nascimento: '))

ano_atual = datetime.date.today().year
idade = ano_atual - nas

print(f'Quem nasce em {nas} tem {idade} anos em {ano_atual}.') 

if idade == 18:
    print('Você teve se alistar IMEDIATAMENTE!')
elif idade < 18:
    ano_alis = 18 - idade
    print(f'Ainda falta {ano_alis} anos para o alistamneto')
    print(f'Seu alistamento será em {ano_atual + ano_alis}')
elif idade > 18:
    ano_alis = idade - 18
    print(f'Você já deveria ter se alistado há {ano_alis}')
    print(f'Seu alistamento foi em {ano_atual - ano_alis}')