
class Filme():
    def __init__(self, titulo, diretor):        
        self.titulo = titulo        
        self.diretor = diretor    
        
    def __str__(self):        
        return self.titulo + ' - ' + self.diretor
    
    def __eq__(self, outro_filme):        
        return self.titulo == outro_filme.titulo and self.diretor == outro_filme.diretor
    
def pega_todos_os_filmes():    
    return [
        Filme('A Teoria de Tudo' , 'James Marsh'), 
        Filme('La La Land', 'Damien Chazelle'), 
        Filme('O Poderoso Chefão', 'Francis Ford Coppola'), 
        Filme('The Matrix', 'Watchowsky')
        ]

# meus_filmes = pega_todos_os_filmes()
# for filme in meus_filmes:    
#     print(filme)
    
def tenho_o_filme(filme_procurado):    
    meus_filmes = pega_todos_os_filmes()    
    for filme in meus_filmes:        
        if filme_procurado == filme:            
            return True    
    return False

filme_procurado = Filme('A Teoria de Tudo', 'James Marsh')
if tenho_o_filme(filme_procurado):    
    print('Tenho o filme!')
else:    
    print('Não tenho :(')
    
filme_procurado = Filme('The Matrix', 'Watchowsky')
if tenho_o_filme(filme_procurado):    
    print('Tenho o filme!')
else:    
    print('Não tenho :(')


