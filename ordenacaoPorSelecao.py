def buscaMenorIndice(arr):
    menor = arr[0]
    menorIndice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menorIndice = i

    return menorIndice

def ordenacaoPorSelecao(arr):
    novoArray = []

    for i in range(len(arr)):
        menorIndice = buscaMenorIndice(arr)
        novoArray.append(arr.pop(menorIndice))
    return novoArray

print(ordenacaoPorSelecao([5,3,6,2,10]))
