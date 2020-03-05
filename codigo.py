class Conta():
    def __init__(self, nome):
        self.__nome = nome
        self.__saldo = 0


    #método getter
    def get_nome(self):
        return self.__nome

    def get_saldo(self):
        return self.__saldo

    #método set
    def set_nome(self, nome):
        self.__nome = nome

    def set_saldo(self, valor):
        self.__saldo = valor

    def __str__(self):
        return "{} tem R${}".format(self.__nome, self.__saldo)

gabriel = Conta("gabriel")

print(gabriel)

gabriel.set_saldo(90)
print(gabriel)
print(vars(gabriel))
