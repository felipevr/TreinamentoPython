#import datetime
from datetime import timedelta, datetime


class Cadastro:
    def __init__(self):
        self.data_cadastro = datetime.today()
        
    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=15, minutes=20,seconds=30)
        return agora - self.data_cadastro
    
    
a = Cadastro()
b = a.tempo_cadastro()
print(b)


