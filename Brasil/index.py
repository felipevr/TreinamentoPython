# Formação Python e orientação a objetos
# Curso Python Brasil: validação de dados nacional
# https://cursos.alura.com.br/course/python-validacao-dados/task/62231

from validate_docbr import CPF
from Cpf import Cpf



cpf = '13876724872'
# cpf = '22222222222'
# cpf = CPF().generate()
# print(cpf)

objeto_cpf = Cpf(cpf)

print(objeto_cpf)




