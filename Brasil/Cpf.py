class Cpf:
    def __init__(self, documento):
        self._documento = str(documento)
        if not self.cpf_eh_Valido(self._documento):
            raise ValueError("CPF inválido!!")
    
    def __str__(self):
        return self.format_cpf()
    
    def cpf_eh_Valido(self, documento):
        if (len(documento) == 11):
            return True
        else:
            return False
        
    def format_cpf(self):
        cpf = self._documento
        fatia_um = cpf[:3]
        fatia_dois = cpf[3:6]
        fatia_tres = cpf[6:9]
        fatia_quatro = cpf[9:]

        return "{}.{}.{}-{}".format(
            fatia_um, fatia_dois, fatia_tres, fatia_quatro
        )
