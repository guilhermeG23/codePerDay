teste1 = {"teste1":1, "teste2":2}
teste2 = dict(teste1 = 1, teste2 = 2)

#Usando lista
print(type(teste1))
print(teste1)
print(teste2)
print(teste1['teste1'])
print(teste2['teste1'])

#Confirma se chave existe
#Confirma, se nao existe, retorna 0
print(teste1.get("teste3", 0))
#E se existe
print(teste1.get("teste2", 0))

#Adicionando
teste1["teste3"] = 3
print(teste1)

#Alterando
teste1["teste3"] = 4
print(teste1)

#deletando
del teste1["teste3"]
print(teste1)

#Buscando se existe dentro da chave
print("teste2" in teste1)

#Imprimindo
for i in teste1:
    print("{}: {}".format(i, teste1[i]))

#Chaves
for i in teste1.keys():
    print(i)

#Valores
for i in teste1.values():
    print(i)

#Duplas - items
for i, t in teste1.items():
    print("{}: {}".format(i, t))
