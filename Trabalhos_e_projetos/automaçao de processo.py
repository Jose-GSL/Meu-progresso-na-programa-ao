'''Primeiro ele vai pegar os nomes dos protudose em um site e colocar no exel, depois pegar os preços e colocar ao lado dos nomes,
apos terminar esse processo vai enviar um email para o email da pessoa relado o termino do processo'''

import requests as rq
from bs4 import BeautifulSoup as bs
import os  
import pandas  as pd
import openpyxl as pp


'''PASSO 1:qual sera o site a onde pagara o nome e o protudo'''
url = str(input('Digite o url a o lado: '))

#forma de acessar o site,pegar as informações do site 
acesso = rq.get(url)

#Uma forma de organizar as informaçoes do site, e transforma na linguagem python
site_organizado = bs(acesso.text, 'html.parser')
nome_protudo = site_organizado.find('h3')
print(nome_protudo.text)




