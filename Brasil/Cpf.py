from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        self._documento = str(documento)
        self.__validador = CPF(repeated_digits=True)
        if not self.cpf_eh_Valido(self._documento):
            raise ValueError("CPF inválido!!")
    
    def __str__(self):
        return self.format_cpf()
    
    def cpf_eh_Valido(self, documento):
        if len(documento) != 11:
            raise ValueError("Quantidade de digitos incorreta")
                
        return self.__validador.validate(documento)
                
    def format_cpf(self):
        cpf = self._documento
        
        return self.__validador.mask(cpf)
