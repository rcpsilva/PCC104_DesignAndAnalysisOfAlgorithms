class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root,value)

    def _insert(self,node,value):
        if value > node.value:
            if node.right == None:
                node.right = Node(value)
            else:
                self._insert(node.right,value)
        elif value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self._insert(node.left,value)
