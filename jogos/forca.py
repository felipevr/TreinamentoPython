#!/usr/bin/python
# curso alura
# https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/
def hello():

    print(""" 
    *************************************
    * Bem vindo ao jogo de Forca! *
    *************************************
    """)


def jogar():
    
    hello()
    
    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        print("Jogando...")


    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()