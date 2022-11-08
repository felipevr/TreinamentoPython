#!/usr/bin/python
from extrator_url import ExtratorURL

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = "https://bytebank.com/cambio?moedaOrigem=dolar2&moedaDestino=real&quantidade=10"
#url = ' '
#url = None
#url = "https://bytebank.co/aa?v"

extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print("O tamanho da URL: ", len(extrator_url))
print("URL completa: ", extrator_url)

print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)

valor_quantidade = int(extrator_url.get_valor_parametro("quantidade"))
print("Valor: ", valor_quantidade)

moeda_origem  = extrator_url.get_valor_parametro("moedaOrigem")
print("De: ", moeda_origem )

moeda_destino  = extrator_url.get_valor_parametro("moedaDestino")
print("Para: ", moeda_destino )

VALOR_DOLAR = 5.5 #reais

if (moeda_origem  == 'real' and moeda_destino == "dolar"):
    resultado = valor_quantidade / VALOR_DOLAR
elif moeda_origem == "dolar" and moeda_destino == "real":
    resultado = int(valor_quantidade) * VALOR_DOLAR
    #print("O valor de $" + valor_quantidade + " dólares é igual a R$" + str(resultado) + " reais.")
else:
    raise ValueError(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")


print('Valor resultante: ', resultado, moeda_destino , '(s)')