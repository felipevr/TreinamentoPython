from codigo.bytebank import Funcionario

#lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)

#print(lucas.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print('Teste = {}'.format(funcionario_teste.idade()))
    
    funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
    print('Teste = {}'.format(funcionario_teste1.idade()))
    
    funcionario_teste1 = Funcionario('Teste', '11/08/1999', 1111)
    print('Teste = {}'.format(funcionario_teste1.idade()))
    
#teste_idade()


ana = Funcionario('Ana', '12/03/1997', 100000)

print(ana.calcular_bonus())


