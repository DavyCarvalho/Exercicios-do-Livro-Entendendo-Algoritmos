book = dict()

book["maca"] = 0.67
book["leite"] = 1.49
book["abacate"] = 1.49

print(book)

lista_telefonica = {}

lista_telefonica["jenny"] = 8675309
lista_telefonica["emergency"] = 911

print(lista_telefonica["jenny"])

votaram = {}
valor = votaram.get("tom")

def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        votaram[nome] = True
        print( "Deixe votar!")

# cache = {}
# def pega_pagina(url):
#     if cache.get(url):
#         return cache[url] ❶
#     else:
#         dados = pega_dados_do_servidor(url)
#         cache[url] = dados ❷
#         return dados
