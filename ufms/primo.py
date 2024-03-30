def numero_primo(numero):
    contador = 0
    for i in range(1, numero + 1, 1):
        if numero % i == 0:
            contador += 1
    return contador == 2
    
def verifica_se_numeros_informados_sao_primos():
    numero = int(input("Digite um numero inteiro positivo:"))
    while (numero != 0):
        if numero > 2 and numero % 2 == 0:
            print("O numero ", numero, "não é primo")
        
        if numero_primo(numero):
            print("O numero", numero, "é primo")
        else:
            print('o numero', numero, "nao é primo")
        numero = int(input("Digite outro numero inteiro positivo:"))
        
def gera_x_numeros_primos(quantidade = 0, inicial = 1):
    if quantidade == 0:
        quantidade = int(input("Digite um numero inteiro positivo:"))
    contador = 0
    inteiro = inicial
    #for i in range(quantidade+1):
    while contador < quantidade:
        if numero_primo(inteiro):
            contador += 1
            print(inteiro, end=', ', flush=True)
        inteiro += 1
        
gera_x_numeros_primos(2000, 144671)