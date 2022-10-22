
class Cliente:

    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @property
    def email(self):
        return self.__email.lower()

    def __str__(self) -> str:
        return self.__nome.title() + ' : ' + str(self.__idade) + ' : ' + self.__email