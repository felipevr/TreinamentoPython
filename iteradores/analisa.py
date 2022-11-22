
# with open("acessos.log", 'r') as registro:
#     sites_sem_https = [url for url in registro if url.startswith('http://')]

#     print(sites_sem_https[0])



class IteradorHttp():
    def __init__(self, arquivo):
        self.registro = open(arquivo, 'r')
        self.linha_atual = ''
    def __iter__(self):
        return self
    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual
        raise StopIteration

iterador = IteradorHttp('acessos2.log')

# for i in range(1000):
#     print(i, next(iterador))

# a = next(iterador, False)
# i = 1
# while a:
#     print(i, a)
#     i += 1
#     a = next(iterador, False)
    
i = 1
for url in iterador:
    print(i, url)
    i += 1
    
    
    
    