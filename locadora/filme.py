from acervo import Acervo
class Filme (Acervo):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

    def retorna_cadastro_diferenciado(self):
        pass
