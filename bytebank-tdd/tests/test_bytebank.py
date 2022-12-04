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