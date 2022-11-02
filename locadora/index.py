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
demo = Serie('Demolidor', 2016, 2)

demo.dar_like()
demo.dar_like()
demo.dar_like()
todo.dar_like()
todo.dar_like()
todo.dar_like()
todo.dar_like()
todo.dar_like()



acervos = [vingadores, atlanta, demo, todo]

pl_fds = Playlist('fim de semana', acervos)

for item in pl_fds:
    print(item)

