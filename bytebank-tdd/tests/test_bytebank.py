# https://docs.pytest.org/en/7.1.x/how-to/mark.html
#comando para verificiar cobertura 
# pytest --cov=codigo tests/
from codigo.bytebank import Funcionario
import pytest, sys
from pytest import mark

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
        
    def test_quando_nome_recebe_lucas_carvalho_deve_retornar_lucas(self):
        entrada = ' Lucas Carvalho ' #Dado
        esperado = 'Lucas Carvalho'
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        
        resultado = lucas.nome # Quando
        
        assert resultado == esperado #Então
        
    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_caravalho(self):
        entrada = ' Lucas Carvalho ' #Dado
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        
        resultado = lucas.sobrenome() # Quando
        
        assert resultado == esperado #Então
        
        
    @mark.skip
    def test_que_nao_deve_ser_executado(self):
        assert 1 == 1
        
    @mark.xfail(True, reason="Teste")
    def test_que_deve_falhar(self):
        assert True == False
        
    @pytest.mark.skipif(sys.version_info < (3, 1), reason="Requer Python na versão 3")
    def test_eh_python_3(self):
        assert True
    
    
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        
        funcionario_teste = Funcionario(entrada_nome, '11/11/1990', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario
        
        assert resultado == esperado #Então
        
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        esperado = 100
        
        funcionario_teste = Funcionario('teste', '11/11/1990', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()
        
        assert resultado == esperado #Então
        
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        #Esperado
        with pytest.raises(Exception):
            entrada_salario = 1000000 #Given
            
            funcionario_teste = Funcionario('teste', '11/11/1990', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()
            
            #assert resultado == esperado #Então
            
    
        
    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Lucas Carvalho', '13/02/1999', 1000 #Dado - entrada
        esperado = f'Funcionario({nome}, {data_nascimento}, {salario})'
        
        func = Funcionario(nome, data_nascimento, salario)
        
        resultado = func.__str__() # Quando
        
        assert resultado == esperado #Então