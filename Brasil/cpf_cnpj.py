from validate_docbr import CPF
from validate_docbr import CNPJ


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self._tipo_documento = tipo_documento
        self._documento = str(documento)
        if tipo_documento == 'cpf':
            self.__validador = CPF(repeated_digits=True)
            if not self.cpf_eh_Valido(self._documento):
                raise ValueError("CPF inválido!!")
        elif tipo_documento == 'cnpj':
            self.__validador = CNPJ()
            if not self.cnpj_eh_Valido(self._documento):
                raise ValueError("CNPJ inválido!!")            
        else:
            raise ValueError("Documento inválido")
        
    
    def __str__(self):
        if self._tipo_documento == 'cpf':
            return self.format_cpf()
        else:
            return self.format_cnpj()
    
    def cpf_eh_Valido(self, documento):
        if len(documento) != 11:
            raise ValueError("Quantidade de digitos incorreta")
                
        return self.__validador.validate(documento)
                
    def format_cpf(self):
        cpf = self._documento
        return self.__validador.mask(cpf)
    
    def format_cnpj(self):
        cnpj = self._documento
        return self.__validador.mask(cnpj)

    def cnpj_eh_Valido(self, cnpj):
        if len(cnpj) != 14:
            raise ValueError("Quantidade de digitos incorreta")
                
        return self.__validador.validate(cnpj)