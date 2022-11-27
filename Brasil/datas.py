#import datetime
from datetime import timedelta, datetime


class Datas:
    
    
    
    def __init__(self):
        self.data_cadastro = datetime.today()
        
    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=15, minutes=20,seconds=30)
        return agora - self.data_cadastro
    
    def mes_cadastro(self):
        mes_cadastro = self.data_cadastro.month
        return mes_cadastro


