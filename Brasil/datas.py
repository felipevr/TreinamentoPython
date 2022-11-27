#import datetime
from datetime import timedelta, datetime


class Datas:
    
    meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
    
    dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
    
    def __init__(self):
        self.data_cadastro = datetime.today()
        
    def __str__(self):
        return self.format_data()
        
    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=15, minutes=20,seconds=30)
        return agora - self.data_cadastro
    
    def mes_cadastro(self):
        mes_cadastro = self.data_cadastro.month
        print(mes_cadastro)
        return self.meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dia_semana = self.data_cadastro.weekday()
        return self.dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
