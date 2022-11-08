import re

class ExtratorURL:
    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self.valida_url()
        self.quebra_url()
        
    @property
    def url(self):
        return self._url
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self):
        if not self._url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self._url)
        if not match:
            raise ValueError('A URL não é válida.')
        
    def quebra_url(self):
        self._indice_interrogacao = self._url.find('?')
        
        if self._indice_interrogacao == -1:
            raise ValueError('A URL não tem parametros')
        
        self._url_base = self._url[:self._indice_interrogacao]
        self._url_parametros = self._url[self._indice_interrogacao+1:]
        
        if not self._url_base.endswith('/cambio'):
            raise ValueError('Esse URL não é da página de cambios')
        
        
    def get_url_base(self):
        # self.indice_interrogacao = self.url.find('?')
        # url_base = self.url[:self.indice_interrogacao]
        return self._url_base
    
    def get_url_parametros(self):
        #indice_interrogacao = self.url.find('?')
        # self.url_parametros = self.url[self.indice_interrogacao+1:]
        return self._url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self._url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_separador = self._url_parametros.find('&', indice_valor)
        if (indice_separador == -1):
            valor = self._url_parametros[indice_valor:]
        else:
            valor = self._url_parametros[indice_valor:indice_separador]
        return valor
    
    def __len__(self) -> int:
        return len(self._url)
    
    def __str__(self) -> str:
        return self._url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self._url == other.url