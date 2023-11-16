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

    def inorder(self):
        elements = []
        self._inorder(self.root,elements)
        return elements

    def _inorder(self,node,elements):
        if node is not None:
            self._inorder(node.left,elements)
            elements.append(node.value)
            self._inorder(node.right,elements)

if __name__ == '__main__':

    tree = BST()

    vals = [1,8,2,6,4,7,3,5]
    
    for v in vals:
        tree.insert(v)

    print(tree.inorder())

    for v in vals:
        print(tree.search(v))

    print(tree.search(10))
    print(tree.search(15))
    print(tree.search(0))






            
