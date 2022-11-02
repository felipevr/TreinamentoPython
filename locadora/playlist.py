class Playlist:
    def __init__(self, nome, lista):
        self._nome = nome
        self._programas = lista

    @property
    def listagem(self):
        return self._programas

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def tamanho(self):
        return len(self._programas)