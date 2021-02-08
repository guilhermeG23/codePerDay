#Class sem _ para manipular direto a variavel
class Teste1:

    def __init__(self, valor):
        self.entrada = valor

    def setValor(self, valor):
        self.entrada = valor
        return True

    def getValor(self):
        print(self.entrada)

#Classe com _ para impedir a manipulação direta
class Teste2:

    def __init__(self, valor):
        self.__entrada = valor

    def setValor(self, valor):
        self.__entrada = valor
        return True

    def getValor(self):
        print(self.__entrada)

#Classe sem _
t1 = Teste1(10)
t1.getValor()
t1.setValor(11)
t1.getValor()
print(t1.entrada)

print("---------------------")

#Class com _
t2 = Teste1(10)
t2.getValor()
t2.setValor(11)
t2.getValor()
try:
    print(t2.__entrada)
except:
    print("Não permite vizualização sobre variavel restrita")
