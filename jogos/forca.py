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
    
    palavra_secreta = "banana" #sempre minuscula

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip()


        index = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index += 1

        print("Jogando...")


    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()