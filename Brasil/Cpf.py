class Cpf:
    def __init__(self, documento):
        self._documento = str(documento)
        if not self.cpf_eh_Valido(self._documento):
            raise ValueError("CPF inválido!!")
            
    
    def cpf_eh_Valido(self, documento):
        if (len(documento) == 11):
            return True
        else:
            return False