class Playlist(list):
    def __init__(self, nome, lista):
        self._nome = nome
        super().__init__(lista)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
