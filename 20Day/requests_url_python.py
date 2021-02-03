"""
Libs necessarias
"""
import requests
import sys

"""
Endereco alvo
"""
#URL Exemplo -> url = "https://www.google.com.br/"
url = sys.argv[1]

"""
Resposta do endereco
"""
reposta = requests.get(url)

"""
Converter o status code da página para int
"""
resposta_code = int(reposta.status_code)

"""
Saida de status
"""
if resposta_code < 300:
    print("Página encontrada com sucesso: {}".format(resposta_code)) #
elif resposta_code >= 300 and resposta_code <= 399:
    print("Página com redirecionamento: {}".format(resposta_code))
elif resposta_code >= 400 and resposta_code <= 499:
    print("Página com erro de cliente: {}".format(resposta_code))
else:
    print("Página com erro do servidor: {}".format(resposta_code))