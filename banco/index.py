from conta import Conta
from datas import Data

# d = Data(21,11,2007)
# d.formatada()

b = Conta.codigos_bancos()
c = Conta.codigos_bancos('BB')
d = Conta.codigos_bancos('asd')

conta = Conta(123, "Nico", 55.0, 1000.0) 

print('aa:', conta.codigo_banco())

conta2 = Conta(1243, "Marc", 545.0, 10000.0) 

print(conta2)

print(Conta.codigo_banco())

conta.deposita( 15.0)
conta.extrato()
#Saldo é 70.0
conta.saca(20.0)
conta.extrato()
#Saldo é 50.0
conta.saca(200) 
conta.extrato()
conta.saca(200)
conta.extrato()
print(conta.limite_disponivel)
print(conta.limite_total)

# print(conta._Conta__limite)
# conta._Conta__limite = 666
# print(conta._Conta__pode_sacar(1222))
# print(conta._Conta__limite)

