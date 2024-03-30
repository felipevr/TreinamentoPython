from random import randint
import time


def funcao_quadratica(n):
    soma = 0
    #n = int(input('numero inteiro:'))
    for i in range(1,n+1):
        for j in range(1,n+1):
            aleatorio = randint(1,1000)
            soma = soma + aleatorio
    print("resultado", soma)
    
def funcao_cubica(n):
    soma = 0
    #n = int(input('numero inteiro:'))
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                aleatorio = randint(1,1000)
                soma = soma + aleatorio
    print("resultado", soma)

tenta = [10, 100, 1000]

print('funcao quadratica')
for k in tenta:
    inicio = time.time()

    funcao_quadratica(k)

    fim = time.time()
    print("10: ", fim - inicio)
    

print('funcao cubica')
for k in tenta:
    inicio = time.time()

    funcao_cubica(k)

    fim = time.time()
    print(k, ": ", fim - inicio)
    
    
"""
funcao quadratica
resultado 45192
10:  0.0
resultado 4972344
100:  0.0060062408447265625
resultado 500321691
1000:  0.5779690742492676
funcao cubica
resultado 504308
10:  0.0010020732879638672
resultado 500886443
100:  0.5159964561462402
resultado 500509069738
1000:  552.0476648807526
"""