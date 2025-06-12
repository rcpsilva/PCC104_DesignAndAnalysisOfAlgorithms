class HeapPQ:
    """Uma fila de prioridade mínima baseada em heap binário."""

    def __init__(self):
        """Inicializa uma fila de prioridade vazia."""
        self._entries = []

    def insert(self, item, priority):
        """Insere um novo item na fila de prioridade com a prioridade dada.

        Args:
            item (Any): O item a ser inserido.
            priority (int | float): A prioridade associada ao item. Menor valor indica maior prioridade.
        """
        self._entries.append((item,priority))
        self._upheap(len(self._entries)-1)

    def _parent(self, i):
        """Retorna o índice do pai de um nó no heap.

        Args:
            i (int): Índice do nó filho.

        Returns:
            int: Índice do nó pai.
        """
        
        return (i-1)//2

    def _children(self, i):
        """Retorna os índices dos filhos de um nó no heap.

        Args:
            i (int): Índice do nó pai.

        Returns:
            range: Índices válidos dos filhos.
        """
        pass

    def _upheap(self, i):
        """Sobe um elemento na árvore até restaurar a propriedade do heap.

        Args:
            i (int): Índice do elemento a ser ajustado.
        """
        

        if i == 0:
            return
        
        parent = self._parent(i)
        if self._entries[parent][1] >= self._entries[i][1]:
            return
        else:
            self._entries[parent], self._entries[i] = self._entries[i], self._entries[parent]  
            return self._upheap(parent)

    def findmin(self):
        """Retorna o item com menor prioridade sem removê-lo da fila.

        Returns:
            Any: O item com maior prioridade (menor valor de prioridade).
        """
        pass

    def removemin(self):
        """Remove e retorna o item com menor prioridade da fila.

        Returns:
            Any: O item removido com a maior prioridade.
        """
        pass

    def _downheap(self, i):
        """Desce um elemento na árvore até restaurar a propriedade do heap.

        Args:
            i (int): Índice do elemento a ser ajustado.
        """
        pass

    def __len__(self):
        """Retorna o número de elementos na fila de prioridade.

        Returns:
            int: Número de elementos.
        """
        return len(self._entries)

if __name__ == '__main__':
    pq = HeapPQ()

    # Inserções com diferentes prioridades
    pq.insert("task A", 4)
    pq.insert("task B", 2)
    pq.insert("task C", 5)
    pq.insert("task D", 1)
    pq.insert("task E", 3)
    pq.insert("task F", 4)
    pq.insert("task G", 5)
    pq.insert("task H", 6)
    pq.insert("task I", 7)
    pq.insert("task J", 8)
    pq.insert("task K", 9)
    pq.insert("task L", 10)

    print(f"Tamanho da fila: {len(pq)}")  # Deve ser 5

    print(pq._entries)

    #print(f"Item de maior prioridade: {pq.findmin()}")  # Deve ser "task D"

    # Remoções sucessivas
    #while len(pq) > 0:
    #    print(f"Removido: {pq.removemin()}")
