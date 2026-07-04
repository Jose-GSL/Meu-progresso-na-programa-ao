'''Impostações necessaria para o codigo funcionar'''
import requests as rq 
from bs4 import BeautifulSoup as bs
import os

os.makedirs('resultado',exist_ok= True)#cria uma pasta para o projeto, quanqeunto garante que a pasta exitia

'''O codigo puxara de um site e coletara os dados que tenha no site, podendo adquirir dados de vendas e 
organizalos em um pasta.'''

'''Primeiro onde vai esta o site que tem que acessar'''
url = 'https://www.eviltester.com/'# local do site, onde a informaçoes entao 

'''Como ele vai acessar esse saite'''
resposta = rq.get(url) #pega o site e a informaçao bruta do site 

site_organizado = bs(resposta.text, 'html.parser')#Esse codigo ajuda traduzir o site para o python e faciita a leituram em html

todos_h2 = site_organizado.find_all('h2')# Serve para encontar o primeiro codigo da pagina que começa com h1,podendo ser mudado a qualquer momento, o que e pedido 


with open ('resultado/dados_text.text','w') as arquivo:#Com o with open ele abre uma pasta  com o nomme 'dados_text.text' e ercreve com o w e dar o nome de arquivo
    for item in todos_h2:
        arquivo.write(item.text + '\n') # E com o esse escreve o resultado_text (que e o que esta escrito no site) no arquivo 