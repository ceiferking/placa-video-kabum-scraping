from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.chrome.options import Options
import math

#recebe link da kabum onde queira extrair dados
site_link = input('Cole aqui o link do site da kabum do tipo de item que queira buscar: ') 

opitions = Options()
#oculta navegador
opitions.add_argument('==headdless') 
#define tamanho do navegador
opitions.add_argument('window-size=400,800')
#carrega o web drive do navegador
navegador = webdriver.Chrome(options=opitions)
#acessa o site disponibilisado pelo usuario
navegador.get(site_link) 

sleep(4) #aguarda o conteudo da pagina ser carregado.

#recebe o conetudo do site
page_contante = navegador.page_source 

site = BeautifulSoup(navegador.page_source, 'html.parser')

lista_items = site.find('div',id='listingCount').get_text().strip()

index = lista_items.find(' ')
qtd_items_total = lista_items[:index]
#faz a quantidade de paginas necessarias que devera ser extraida
numero_de_paginas = math.ceil(int(qtd_items_total)/20)
#cria o dicionario
dic_produtos = {'marca':[], 'preco':[], 'ref':[]} 

#caminha entre todos as paginas de produtos e solicita informacoes
for i in range(1, numero_de_paginas+1):
    url_pag = f'{site_link}?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    produto = site.find_all('div', class_=re.compile('productCard'))

    #Extrai as informaçoes dos produtos descrição, preco, link
    for produto in produto:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco =  produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        link = produto.find('a', class_='sc-brCFrO bkMjYu')
        #obtem o link fragmentado individual do item
        link1 = link['href']
        #Soma a url do item e do site para criar o link do produto
        link1 = f'https://www.kabum.com.br{link1}'

        print(marca, preco, link1)

        #salva as informaçoes estraidas no dicionario criado
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)
        dic_produtos['ref'].append(link1)


df = pd.DataFrame(dic_produtos)
df.to_csv('placas_pd.csv', encoding='utf-8', sep=';')