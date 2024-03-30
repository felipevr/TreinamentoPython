
# Finalmente, quanto mais modularizado for o seu programa, melhor. 
# Em outras palavras, tente desenvolver uma função para a leitura inicial dos produtos e seu preço e outra para a busca do preço de um certo produto
def leitura_inicial():
    # lê uma quantidade n de frutas ou verduras a serem precificadas. 
    n = int(input())
    # Lida essa quantidade, seu programa deve ler os n produtos em si, juntamente com o preço de cada um deles e guardá-los em uma lista. 
    # Obs.: utilize somente uma lista (vide videoaulas 3 da Unidade 2 do Módulo 2 da disciplina) para armazenar os produtos e seus preços
    lista = []
    for i in range(n):
        produto = input()
        preco = input()
        item = (produto, preco)
        #Atenção: caso o produto já tenha sido cadastrado, a mensagem “Produto já cadastrado" deve aparecer na tela
        if item in lista:
            print('Produto já cadastrado')
        else:
            lista.append( item )
    return lista

# Feito cadastro dos produtos, seu programa deve em seguida ler o nome de vários hortifrutis 
# e imprimir o seu preço caso o produto esteja na lista lida inicialmente. 
def varios_hortifrutis(lista):
        
    hortifruti = input()
    
    while hortifruti:
        # A busca pelo preço de um produto deve ser feita enquanto o usuário não digitar a palavra “Fim”. Lembre-se que a linguagem Python diferencia letras maiúsculas das minúsculas. 
        if hortifruti == 'Fim':
            break
        
        item = busca_produto(hortifruti, lista)
        # Caso ele não esteja na lista, seu programa deve imprimir a mensagem “Produto não cadastrado”.
        if item is None:
            print("Produto nao cadastrado")
        else:
            print(item[1])
            
        hortifruti = input()


def busca_produto(hortifruti, lista):
    
    for item in lista:
        if hortifruti == item[0]:
            return item
    
    return None


lista = leitura_inicial()
varios_hortifrutis(lista)
