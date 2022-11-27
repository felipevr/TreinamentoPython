import re

class TelefonesBR:

    def __init__(self, phone) -> None:
        self.phone_pattern = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        if self.phone_is_valid(phone):
            self.phone = re.search(self.phone_pattern, phone)
        else:
            raise TelefoneInvalido('Verifique o número de digitos colocados')

    def phone_is_valid(self, phone):
        if re.findall(self.phone_pattern, phone):
            return True
        else:
            return False

    def masked(self):
        if self.phone.group(1):
            masked_phone = '+{phone_part[1]}({phone_part[2]}){phone_part[3]}-{phone_part[4]}'.format(phone_part=self.phone)
        else:            
            masked_phone = '+55({phone_part[2]}){phone_part[3]}-{phone_part[4]}'.format(phone_part=self.phone)

        return masked_phone

    def __str__(self) -> str:
        return self.masked()


class TelefoneInvalido(Exception):
    pass
