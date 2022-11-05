class Playlist:
    def __init__(self, nome, lista):
        self._nome = nome
        self._programas = lista

    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
