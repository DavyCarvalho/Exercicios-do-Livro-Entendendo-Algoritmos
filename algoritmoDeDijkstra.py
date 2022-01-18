grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2
grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}

infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

vertices_processados = []

def ache_vertice_com_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    vertice_custo_mais_baixo = None
    for vertice in custos: 
        custo = custos[vertice]
    if custo < custo_mais_baixo and vertice not in vertices_processados: 
        custo_mais_baixo = custo 
        vertice_custo_mais_baixo = vertice
    return vertice_custo_mais_baixo

vertice = ache_vertice_com_custo_mais_baixo(custos) 
while vertice is not None: 
    custo = custos[vertice]
    vizinhos = grafo[vertice]
    for n in vizinhos.keys(): 
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo: 
            custos[n] = novo_custo 
            pais[n] = vertice 
    vertices_processados.append(vertice) 
    vertice = ache_vertice_com_custo_mais_baixo(custos)
