#!/usr/bin/python
# https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos

from filme import Filme
from serie import Serie


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2) 
#atlanta.nome= 'iba daba du'

atlanta.dar_like()
atlanta.dar_like()
  
# print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')


acervos = [vingadores, atlanta]

for item in acervos:
    print(item)

