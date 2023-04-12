class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if not current_node.left:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if not current_node.right:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("Value already in tree.")

    def search(self, data):
        if self.root:
            found = self._search(data, self.root)
            if found:
                return True
            return False
        else:
            return None

    def _search(self, data, current_node):
        if data == current_node.data:
            return True
        elif data < current_node.data and current_node.left:
            return self._search(data, current_node.left)
        elif data > current_node.data and current_node.right:
            return self._search(data, current_node.right)
        return False

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

