print(""" 
*************************************
* Bem vindo ao jogo de Adivinhação! *
*************************************
""")

numero_secreto = 42

tentativas_restantes = 3

while (tentativas_restantes > 0):

    chute_str = input("Digite o seu número: ")

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    elif (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

    tentativas_restantes -= 1

    print("Você tem", tentativas_restantes, "tentativas restantes!")


print("Fim do jogo")