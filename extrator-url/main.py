url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = "bytebank.com/cambio?moedaOrigem=real"
#print(url)

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)  # Vai imprimir “bytebank.com/cambio


url_parametros = url[indice_interrogacao+1:]
print(url_parametros)