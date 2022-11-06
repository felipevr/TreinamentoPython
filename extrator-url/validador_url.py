#!/usr/bin/python
import re

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

#url = "www.bytebank.com/cambio"

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

match = padrao_url.match(url)

if not match:
    raise ValueError('A URL não é válida.')

print("A URL é válida")