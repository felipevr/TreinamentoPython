from artigo import Artigo
class Filme (Artigo):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

