# Formação Python e orientação a objetos
# Curso Python Brasil: validação de dados nacional
# https://cursos.alura.com.br/course/python-validacao-dados/task/62231

# from validate_docbr import CPF
from validate_docbr import CNPJ
#from Cpf import Cpf
from cpf_cnpj import CpfCnpj


def testes_cnpj():
    exemplo_cnpj = '91778481072370'
    # cnpj = CNPJ()
    # print(cnpj.validate(exemplo_cnpj))
    # print(cnpj.generate())

    documento = CpfCnpj(exemplo_cnpj, 'cnpj')

    print(documento)



def testes_cpf():
    cpf = '13876724872'
    # cpf = '22222222222'
    # cpf = CPF().generate()
    # print(cpf)

    objeto_cpf = CpfCnpj(cpf, 'cpf')

    print(objeto_cpf)



testes_cnpj()
testes_cpf()

