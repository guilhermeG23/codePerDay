#{} = Conjunto
#Conjuntos são diferentes de lista, aqui não tem controle de posicoes, somente controle de não repetição de elementos
valor1 = {1,2,3,4}
valor2 = {3,4,5,6}
print(type(valor1))
saida = valor1 | valor2 #Busca os que nao repetem
print(saida)
saida = valor1 & valor2 #Busca os que repetem
print(saida)

#Adicionando um valor no conjunto
saida.add(7)
print(saida)

#travando o conjunto
saida = frozenset(saida) #Proposito geral
#saida.add(8) #Acusa erro
print(saida)
