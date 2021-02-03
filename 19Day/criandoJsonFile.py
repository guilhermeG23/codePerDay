"""
Lib necessaria
"""
import json

"""
Entrada formatada JSON
"""
texto = {
    "t1" : "teste1",
    "t2" : "teste2"
}

"""
Criando o arquivo JSON
"""
with open("dados.json", "a") as saida_json:
    """
    Fazendo a entrada de dados em formato JSON
    """
    json.dump(texto, saida_json, indent=4)