#!/usr/bin/python
from extrator_url import ExtratorURL

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

#url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
#url = ' '
#url = None
url = "https/byte/a?v"

extrator_url = ExtratorURL(url)
#extrator_url = ExtratorURL("   ")
valor_quantidade = extrator_url.get_valor_parametro("moedaOrigem")
print(valor_quantidade)

