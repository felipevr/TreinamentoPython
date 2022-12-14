# Formação Python e orientação a objetos
# Curso Python Brasil: validação de dados nacional
# https://cursos.alura.com.br/course/python-validacao-dados/task/62231

# from validate_docbr import CPF
from validate_docbr import CNPJ
#from Cpf import Cpf
from cpf_cnpj import Documento
from acesso_cep import BuscaEndereco
from datas import Datas

def testes_data():
    cadastro = Datas()
    t = cadastro.tempo_cadastro()
    print(t)
    print(cadastro) 
    print(cadastro.mes_cadastro())
    print(cadastro.dia_semana())

    hoje = cadastro.data_cadastro
    hoje_formatada = hoje.strftime("%d/%m/%Y")


    print(hoje)
    print(hoje_formatada)


def testes_cep():
    cep = '01001000'
    objeto_cep = BuscaEndereco(cep)
    print(objeto_cep)

    bairro, cidade, uf = objeto_cep.consulta_cep()
    
    print(bairro, cidade, uf)


def testes_cnpj():
    exemplo_cnpj = '91778481072370'
    # cnpj = CNPJ()
    # print(cnpj.validate(exemplo_cnpj))
    # print(cnpj.generate())

    documento = Documento.cria_documento(exemplo_cnpj)
    print(type(documento))
    print(documento)



def testes_cpf():
    cpf = '13876724872'
    # cpf = '22222222222'
    # cpf = CPF().generate()
    # print(cpf)

    objeto_cpf = Documento.cria_documento(cpf)
    print(type(objeto_cpf))
    print(objeto_cpf)


testes_cnpj()
testes_cpf()
testes_cep()
testes_data()


