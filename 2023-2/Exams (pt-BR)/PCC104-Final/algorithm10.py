def algoritmo(lista, inicio, fim):
    if fim - inicio <= 1:
        return lista[inicio]

    terco = (fim - inicio) // 3
    max1 = algoritmo(lista, inicio, inicio + terco)
    max2 = algoritmo(lista, inicio + terco, inicio + 2 * terco)
    max3 = algoritmo(lista, inicio + 2 * terco, fim)

    return max(max1, max2, max3)