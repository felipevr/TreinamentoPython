from acervo import Acervo

class Serie (Acervo):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'
