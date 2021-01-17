#Alguns trabalhos com listas
teste1 = [1,2,3,4,5]
teste2 = []
teste2 = teste2 + teste1 #Juntando listas por soma
teste3 = teste1.copy() #Copiando os valores da lista
teste4 = []
teste4.extend(teste1) #Fazendo referencia a lista
teste5 = teste1 #Atribuindo a uma variavel

print(teste1)
print(teste2)
print(teste3)
print(teste4)
print(teste5)

"""
No teste 5 tem um problema, voce esta pegando a referencia de 
memoria dele, isso é, afeta o original, tenta dar um valor para ele
"""

teste5.append('a')

print(teste1)
print(teste5)

"""
Ve se ocorre na copia
"""

teste3.append('b')
print(teste1)
print(teste3)