class Node:
    def __init__(self, value):
        """Inicializa um nó da árvore com o valor fornecido.

        Args:
            value (int): Valor armazenado no nó.
        """
        self.value = value
        self.left = None
        self.right = None

class BST():

    def __init__(self):
        """Inicializa uma Árvore Binária de Busca (BST) vazia."""
        self.root = None

    def insert(self, value):
        """Insere um valor na Árvore Binária de Busca.

        Args:
            value (int): Valor a ser inserido na árvore.
        """
        pass

    def remove(self, value):
        """Remove um valor da Árvore Binária de Busca, se presente.

        Args:
            value (int): Valor a ser removido da árvore.
        """
        pass

    def search(self, value):
        """Procura um valor na Árvore Binária de Busca.

        Args:
            value (int): Valor a ser procurado na árvore.

        Returns:
            bool: True se o valor estiver presente, False caso contrário.
        """
        pass

    def height(self):
        """Calcula a altura da árvore.

        Returns:
            int: A altura da árvore (maior número de arestas entre a raiz e uma folha).
        """
        pass

    def inorder(self):
        """Retorna uma lista com os valores da árvore em ordem crescente (inordem).

        Returns:
            list: Lista com os valores da árvore em ordem crescente.
        """
        pass

    def postorder(self):
        """(Executa percurso pós-ordem a partir do valor dado.
        
        OBS: O nome sugere que deveria ser um percurso pós-ordem completo. 
        Pode precisar de ajuste dependendo da intenção real do exercício.

        Returns:
            list: Lista com os valores visitados no percurso pós-ordem.
        """
        pass

       
if __name__ == '__main__':

    tree = BST()

    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.insert(9)
    tree.insert(8)
    tree.insert(7)
    tree.insert(3)
    tree.insert(5)
    tree.insert(6)

    print(tree.inorder())

    print(tree.search(1))
    print(tree.search(2))
    print(tree.search(3))
    print(tree.search(4))
    print(tree.search(5))
    print(tree.search(6))
    print(tree.search(7))
    print(tree.search(8))
    print(tree.search(9))

    print(tree.search(10))
    print(tree.search(11))

    print(f'height {tree.height()}')

