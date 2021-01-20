#Lib necessaria
import requests

#Experimenta
try:
    #Request
    r = requests.get("https://www.google.com")
    #Status da pagina web
    if str(r.status_code) == "200":
        print("Conectada")
    #Confirmar se conexao esta funcionando
except requests.exceptions.ConnectionError:
    print("Desconectada")
