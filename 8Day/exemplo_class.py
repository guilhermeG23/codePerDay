#Construindo uma classe
class Teste:

    #Construtor
    def __init__(self, t1, t2):
        self.setEntrada1(t1)
        self.setEntrada2(self.tratamentoSimples(t2))

    #Quando chamado a class, ira retorna a string
    def __str__(self):
        return "{}-{}".format(self.getEntrada1(), self.getEntrada2())

    #Tratamento simples
    def tratamentoSimples(self, entrada):
        return "{}-bonus".format(entrada)

    #Setters
    def setEntrada1(self, entrada):
        self.entrada1 = entrada
    
    def setEntrada2(self, entrada):
        self.entrada2 = entrada

    #Getters
    def getEntrada1(self):
        return self.entrada1
    
    def getEntrada2(self):
        return self.entrada2

#Requisitando a classe
teste = Teste("t1", "t2")
print(teste)
print(teste.tratamentoSimples("teste"))
print(teste.getEntrada1())
print(teste.getEntrada2())

    