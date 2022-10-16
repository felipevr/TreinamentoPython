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
    letras_acertadas = ["_"] * len(palavra_secreta)

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip()


        index = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra):
                letras_acertadas[index] = letra
                #print("Encontrei a letra {} na posição {}".format(letra, index))
            index += 1

        print(letras_acertadas)
        #print("Jogando...")


    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()