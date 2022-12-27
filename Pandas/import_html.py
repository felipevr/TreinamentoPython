"""
No próximo vídeo o instrutor mostra alguns exemplos de como utilizar o pd.read_html no pandas, para isso, são compartilhados dois links: unafiscosaude.org e federalreserve.gov.

No entanto, no primeiro link, unafiscosaude.org, atualmente, não conseguimos mais ter acesso a tabela mostrada no vídeo, logo você não conseguirá reproduzir o exemplo do instrutor. Então, para não ficar sem um exemplo válido, você poderá seguir um exemplo equivalente.
https://www.federalreserve.gov/releases/h3/current/default.htm

Já quanto ao segundo link, federalreserve.gov, ao tentar ler as tabelas com pd.read_html é retornado um HTTP Error 403, isso se deve pois o método read_html lê apenas aplicações mais simples, então provavelmente ocorreu uma alteração no site e o método do pandas não consegue mais coletar as informações da página facilmente. Desse modo, para fazer a leitura das tabelas do segundo site será necessário realizar um Web Scraping, então você pode copiar e executar o código abaixo no momento do uso do segundo link na aula que você conseguirá coletar as tabelas corretamente:

Obs: É necessário ter instaladas as bibliotecas requests e BeautifulSoup no ambiente python. Para instalá-las, basta executar os códigos nas células do notebook: !pip install requests e !pip install bs4
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.federalreserve.gov/releases/h3/current/default.htm'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
table = soup.findAll('table')
html_file = f'<html><body>{table}</body></html>'
df = pd.read_html(html_file)

# Como a função read_html retorna uma lista de DataFrames, basta acessar as tabelas pelos índices da lista.
# Como temos três tabelas na página usamos os índices 0, 1 ou 2 para acessar os DataFrames que buscamos
print(type(df))