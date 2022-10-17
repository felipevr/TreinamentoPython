from conta import Conta
from datas import Data
d = Data(21,11,2007)
d.formatada()

conta = Conta(123, "Nico", 55.0, 1000.0) 

#print(conta)

conta2 = Conta(1243, "Marc", 545.0, 10000.0) 

print(conta2)
conta2 = None

print(conta2)


conta.deposita( 15.0)
conta.extrato()
#Saldo é 70.0
conta.saca(20.0)
conta.extrato()
#Saldo é 50.0

print(conta._Conta__limite)
conta._Conta__limite = 666
print(conta._Conta__limite)