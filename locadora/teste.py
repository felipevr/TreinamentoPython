from abc import ABC # abstract base classes

from collections.abc import MutableSequence
#from numbers import Complex

class Playlist(MutableSequence):
    pass

#filmes = Playlist()

from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    
    def __str__(self) -> str:
        pass
    
    def __str__(self): 
        pass

class B(Programa):
    pass

x = B()


