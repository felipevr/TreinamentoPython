class Data:

    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        print('{:2d}/{:2d}/{:2d}'.format(self.dia, self.mes, self.ano))