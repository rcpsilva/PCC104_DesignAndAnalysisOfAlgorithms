#include <iostream>
#include <memory>

struct Node {
    int data;
    std::unique_ptr<Node> left;
    std::unique_ptr<Node> right;

    Node(int data) : data(data), left(nullptr), right(nullptr) {}
};

class BST {
private:
    std::unique_ptr<Node> root;

    void insert(std::unique_ptr<Node>& node, int data) {
        if (!node) {
            node = std::make_unique<Node>(data);
        } else if (data < node->data) {
            insert(node->left, data);
        } else if (data > node->data) {
            insert(node->right, data);
        } else {
            std::cout << "Value already in tree." << std::endl;
        }
    }

    bool search(const std::unique_ptr<Node>& node, int data) const {
        if (!node) {
            return false;
        } else if (data == node->data) {
            return true;
        } else if (data < node->data) {
            return search(node->left, data);
        } else {
            return search(node->right, data);
        }
    }

    void inorder(const std::unique_ptr<Node>& node) const {
        if (node) {
            inorder(node->left);
            std::cout << node->data << std::endl;
            inorder(node->right);
        }
    }

public:
    BST() : root(nullptr) {}

    void insert(int data) {
        insert(root, data);
    }

    bool search(int data) const {
        return search(root, data);
    }

    void inorder() const {
        inorder(root);
    }
};


int main() {
    BST bst;

    bst.insert(5);
    bst.insert(3);
    bst.insert(7);
    bst.insert(1);
    bst.insert(9);

    std::cout << bst.search(1) << std::endl; // Output: 1 (true)
    std::cout << bst.search(10) << std::endl; // Output: 0 (false)

    bst.inorder();
    // Output:
    // 1
    // 3
    // 5
    // 7
    // 9

    return 0;
}

