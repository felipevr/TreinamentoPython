# Formação Python e orientação a objetos
# Curso Python Brasil: validação de dados nacional
# https://cursos.alura.com.br/course/python-validacao-dados/task/62231

from Cpf import Cpf

cpf = '15616987913'

objeto_cpf = Cpf(cpf)

print(objeto_cpf)


fatia_um = cpf[:3]
fatia_dois = cpf[3:6]
fatia_tres = cpf[6:9]
fatia_quatro = cpf[9:]

cpf_formatado = "{}.{}.{}-{}".format(
    fatia_um, fatia_dois, fatia_tres, fatia_quatro
)

print(cpf_formatado)