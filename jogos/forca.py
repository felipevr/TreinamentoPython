#!/usr/bin/python
# curso alura
# https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/
import random

def jogar():
    
    mensagem_boas_vindas()
    
    branco = '_'
    palavra_secreta = pega_palavra_secreta() #sempre minuscula
    letras_acertadas = gera_letras_acertadas(palavra_secreta, branco)

    enforcou = False
    acertou = False
    erros = 0
    max_erros = 6

    print(letras_acertadas)

    while(not acertou and not enforcou):
        
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            if (erros < max_erros):
                print("Ops, você errou! Faltam {} tentativas.".format(max_erros-erros))
            

        print(letras_acertadas)
        
        if (branco not in letras_acertadas):
            acertou = True
            continue

        if (erros >= 6):
            enforcou = True

        #letras_faltando = letras_acertadas.count(branco)
        #print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
        
    imprime_msg_final(acertou, palavra_secreta)

def imprime_msg_final(acertou, palavra_secreta):
    if (acertou):
        print('VOCÊ GANHOU ! ! !')
    else:
        print('ENFORCADO!!!')
        print('A palavra era ', palavra_secreta)

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    #print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1

def pede_chute():
    chute = input("Qual letra? ")
    return chute.strip().lower()

def gera_letras_acertadas(palavra, branco = '_'):
    return [branco for letra in palavra]

def mensagem_boas_vindas():

    print(""" 
    *************************************
    * Bem vindo ao jogo de Forca! *
    *************************************
    """)

def pega_palavra_secreta():
    #lista = ['banana', 'maça', 'abacate', 'limão', 'laranja', 'melancia', 'lima', 'jaca', 'açai']
    lista = []

    with open("palavras.txt") as arquivo:
        lista = [linha.strip() for linha in arquivo]

    #print(lista)
    index = random.randrange(0,len(lista))

    return lista[index].lower()



if (__name__ == "__main__"):
    jogar()
