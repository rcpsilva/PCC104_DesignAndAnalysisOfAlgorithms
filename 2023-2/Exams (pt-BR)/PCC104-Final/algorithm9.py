def algoritmo(lista, item, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            return algoritmo(lista, item, inicio, meio - 1)
        else:
            return algoritmo(lista, item, meio + 1, fim)

    return None