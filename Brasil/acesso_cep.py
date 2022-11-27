class BuscaEndereco:
    
    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.cep_eh_Valido(cep):
            self._cep = cep
        else:
            raise ValueError("CEP inválido")
        
    def __str__(self) -> str:
        return self.format_cep()
    
    def cep_eh_Valido(self, cep):
        if (len(cep) == 8):
            return True
        else:
            return False
        
    def format_cep(self):
        return "{}-{}".format(self._cep[:5], self._cep[5:])