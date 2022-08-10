from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.chrome.options import Options
import math

#response = requests.get('https://www.kabum.com.br/hardware/placa-de-video-vga')

opitions = Options()
#opitions.add_argument('==headdless') #oculta navegador
opitions.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=opitions)

navegador.get('https://www.kabum.com.br/hardware/placa-de-video-vga')

sleep(4)

page_contante = navegador.page_source

site = BeautifulSoup(navegador.page_source, 'html.parser')

lista_items = site.find('div',id='listingCount').get_text().strip()

index = lista_items.find(' ')
qtd_items_total = lista_items[:index]

numero_de_paginas = math.ceil(int(qtd_items_total)/20)

dic_produtos = {'marca':[], 'preco':[], 'ref':[]}


for i in range(1, numero_de_paginas+1):
    url_pag = f'https://www.kabum.com.br/hardware/placa-de-video-vga?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    produto = site.find_all('div', class_=re.compile('productCard'))

    
    for produto in produto:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco =  produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        link = produto.find('a', class_='sc-brCFrO bkMjYu')
        link1 = link['href']
        link1 = f'https://www.kabum.com.br{link1}'

        print(marca, preco, link1)

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)
        dic_produtos['ref'].append(link1)



df = pd.DataFrame(dic_produtos)
df.to_csv('placas_pd.csv', encoding='utf-8', sep=';')