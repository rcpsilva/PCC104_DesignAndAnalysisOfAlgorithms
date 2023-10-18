class BST:
    def __init__(self):
        self.root = None

    def search(self,value):
        return self._search(self.root,value)

    def _search(self,node,value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value > node.value:
            return self._search(node.right,value)
        elif value < node.value:
            return self._search(node.left,value)

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None