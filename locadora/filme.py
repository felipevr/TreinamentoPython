from acervo import Acervo
class Filme (Acervo):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):
        pass
