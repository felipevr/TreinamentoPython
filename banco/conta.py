#
# Curso Alura Python: entendendo a Orientação a objeto
# https://cursos.alura.com.br/course/python-3-intro-orientacao-objetos/

from os import stat


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__aba = True
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__bloqueada = False
        self.__ativa = True
        self.__aba = False

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, destino, valor):
        origem = self
        if origem.__pode_sacar(valor):
            origem.saca(valor)
            destino.deposita(valor)

    def __str__(self) -> str:
        if (not self.__aba):
            return "Conta " + str(self.__numero) + ' do ' + self.__titular + ' Saldo: ' + str(self.__saldo) + ' Limite: ' + str(self.__limite)
        else:
            #print(self.__hash__())
            return str(self.__hash__)[-11:-1]

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
        
    @property
    def limite_disponivel(self):
        if (self.__saldo < 0):
            #valor do saldo negativo 
            return self.__limite - abs(self.__saldo)
        else:
            return self.__limite

    @property
    def limite_total(self):
        return self.__limite

    @limite_total.setter
    def limite_total(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos(banco = None):
        codigos = {'BB': '001', 'Caixa':'104', 'Bradesco':'237'}
        if (banco == None):
            return codigos
        elif (banco in codigos):
            return codigos[banco]
        
        return None

