#!/usr/bin/python
# curso alura
# https://cursos.alura.com.br/course/python-introducao-a-linguagem
import random

def hello():

    print(""" 
    *************************************
    * Bem vindo ao jogo de Adivinhação! *
    *************************************
    """)

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    return total_de_tentativas

def main():
    
    total_de_tentativas = hello()
    
    numero_secreto = random.randrange(1, 101)

    pontos = 1000

    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

        rodada += 1



    print("Fim do jogo")


main()