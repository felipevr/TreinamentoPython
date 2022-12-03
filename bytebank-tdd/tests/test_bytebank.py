from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Dado - Contexto
        esperado = 22
        
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        
        # Quando - ação
        resultado = funcionario_teste.idade()
        
        # Então - desfecho
        assert resultado == esperado 
        
        #print('Teste = {}'.format())