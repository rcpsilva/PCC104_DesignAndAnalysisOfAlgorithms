class Node:
    def __init__(self,valor,anterior=None,proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

class LinkedList:
    def __init__(self,inicio):
        self.inicio = inicio

def busca(L,valor):
    x = L.inicio
    while x and x.valor != valor:
        x = x.proximo
    return x

def insere_inicio(L,x):    
    L.inicio.anterior = x
    x.anterior = None
    x.proximo = L.inicio
    L.inicio = x

def insere(x,y):
    x.proximo = y.proximo
    y.proximo = x
    x.anterior = y
    if x.proximo:
        x.proximo.anterior = x
    
if __name__ == "__main__":

    n = Node(2)
    L = LinkedList(n)
    insere_inicio(L,Node(0))
    y = busca(L,0)
    insere(Node(1),y)

