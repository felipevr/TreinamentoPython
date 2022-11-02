
class Acervo:
    base = 5

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @classmethod
    def info(cls):
        return f'A base é {cls.base}'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

    @staticmethod
    def log():
        return f'Isso é um log qualquer'