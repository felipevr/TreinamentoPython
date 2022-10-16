#!/usr/bin/python
# curso alura
# https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/
import random
from re import M

def jogar():
    
    mensagem_boas_vindas()
    
    branco = '_'
    palavra_secreta = pega_palavra_secreta() #sempre minuscula
    letras_acertadas = gera_letras_acertadas(palavra_secreta, branco)

    enforcou = False
    acertou = False
    erros = 0
    max_erros = 7

    imprime_palavra(letras_acertadas)

    while(not acertou and not enforcou):
        
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros, max_erros)
            

        imprime_palavra(letras_acertadas)
        enforcou = erros == max_erros
        acertou = "_" not in letras_acertadas
        
    imprime_msg_final(acertou, palavra_secreta)

def imprime_msg_final(acertou, palavra_secreta):
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        

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

def imprime_palavra(letras_acertadas):
    print(*letras_acertadas, sep=' ')

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

def desenha_forca(erros, max_erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

    if (erros < max_erros):
        print("Ops, você errou! Restam só {} tentativas.".format(max_erros-erros))

def imprime_mensagem_vencedor():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("Parabéns, você ganhou!!!")

def imprime_mensagem_perdedor(palavra_secreta):
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("Você foi enforcado ! ! !")

if (__name__ == "__main__"):
    jogar()
