class ExtratorURL:
    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self._indice_interrogacao = self._url.find('?')
        self.valida_url()
        self._url_base = self._url[:self._indice_interrogacao]
        self._url_parametros = self._url[self._indice_interrogacao+1:]
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self):
        if not self._url:
            raise ValueError('A URL está vazia')
        if self._indice_interrogacao == -1:
            raise ValueError('A URL não tem parametros')
        
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
    