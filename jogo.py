print(""" 
*************************************
* Bem vindo ao jogo de Adivinhação! *
*************************************
""")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

chute = int(chute_str)

#print("Você digitou: ", chute)

print(type(numero_secreto))
print(type(chute))

if (numero_secreto == chute):
    print('Você acertou!')
else:
    print("Você errou!")

print("Fim do jogo")