#!/usr/bin/python
# curso alura
# https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/
import random

def hello():

    print(""" 
    *************************************
    * Bem vindo ao jogo de Forca! *
    *************************************
    """)

def pega_palavra_secreta():
    #lista = ['banana', 'maça', 'abacate', 'limão', 'laranja', 'melancia', 'lima', 'jaca', 'açai']
    lista = []
    arquivo = open("palavras.txt", "r")

    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)

    arquivo.close()

    index = random.randrange(0,len(lista))

    return lista[index].lower()

def jogar():
    
    hello()
    
    branco = '_'
    palavra_secreta = pega_palavra_secreta() #sempre minuscula
    #letras_acertadas = [branco] * len(palavra_secreta)
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip().lower()


        index = 0
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    #print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1
        else:
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))
            erros += 1
            

        print(letras_acertadas)
        
        if (branco not in letras_acertadas):
            acertou = True
            continue

        if (erros >= 6):
            enforcou = True

        #letras_faltando = letras_acertadas.count(branco)
        #print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
        #print("Jogando...")

    if (acertou):
        print('VOCÊ GANHOU ! ! !')
    else:
        print('ENFORCADO!!!')

    #print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()