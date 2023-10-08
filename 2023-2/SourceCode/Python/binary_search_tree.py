class Node:
        self.value = value
        self.left = None
        self.right = None

class BST():

    def __init__(self):
        self.root = None

    def insert(self,value):

        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)

    def search(self,value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value > node.value:
            return self._search(node.right,value)
        elif value < node.value:
            return self._search(node.left,value)

    def inorder(self):
        elements = []
        self._inorder(self.root, elements)
        return elements

    def _inorder(self, node, elements):
        if node is not None:
            self._inorder(node.left, elements)
            elements.append(node.value)
            self._inorder(node.right, elements)

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

