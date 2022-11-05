url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

#url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
#print(url)

#Separa base e os parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmatro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_separador = url_parametros.find('&', indice_valor)
if (indice_separador == -1):
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_separador]

print(valor)