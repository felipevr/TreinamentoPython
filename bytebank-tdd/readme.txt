Repositório do Curso Python e TDD da Alura

https://cursos.alura.com.br/course/python-tdd-explorando-testes-unitarios

h1. Anotações:


Para executar os testes no modo verboso:
# pytest -v


Para verificar a cobertura de código:
# pytest --cov=codigo tests/



Para verificar a cobertura de código:
# pytest --cov=codigo tests/ --cov-report term-missing


Para gerar HTML com a cobertura de código:
# pytest --cov=codigo tests/ --cov-report html

Documentação dos marcadores:
https://docs.pytest.org/en/7.1.x/how-to/mark.html