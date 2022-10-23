class Circulo:

    PI = 3.14

    @staticmethod
    def obter_pi():
        return Circulo.PI


print(Circulo.PI)
print(Circulo.obter_pi())