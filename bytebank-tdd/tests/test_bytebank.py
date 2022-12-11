from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Dado (Given) - Contexto
        esperado = 22
        
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        
        # Quando (When) - ação
        resultado = funcionario_teste.idade()
        
        # Então (Then) - desfecho
        assert resultado == esperado 
        
        #print('Teste = {}'.format())
        
    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_caravalho(self):
        entrada = ' Lucas Carvalho ' #Dado
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        
        resultado = lucas.sobrenome() # Quando
        
        assert resultado == esperado #Então
        
        
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        
        funcionario_teste = Funcionario(entrada_nome, '11/11/1990', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario
        
        assert resultado == esperado #Então
        
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        esperado = 100
        
        funcionario_teste = Funcionario('teste', '11/11/1990', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()
        
        assert resultado == esperado #Então