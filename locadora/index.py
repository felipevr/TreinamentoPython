#!/usr/bin/python
# https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos

from filme import Filme
from serie import Serie
from playlist import Playlist


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2) 

atlanta.dar_like()
atlanta.dar_like()
  
todo = Filme('Todo mundo doido', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
todo.dar_like()
todo.dar_like()
todo.dar_like()
todo.dar_like()
todo.dar_like()



acervos = [vingadores, atlanta, demolidor, todo]

pl_fds = Playlist('fim de semana', acervos)

print(f'Tamanho do playlist: {len(pl_fds)}')

for item in pl_fds:
    print(item)

print('Tá na lista', (demolidor in pl_fds))