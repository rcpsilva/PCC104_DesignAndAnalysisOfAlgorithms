#include <concepts>
#include <iostream>
#include "BinarySearchTree.h"


template<std::totally_ordered T>
class BinarySearchTree {

	class BSTNode {
	public:
		T value;
		std::unique_ptr<BSTNode> left;
		std::unique_ptr<BSTNode> right;

		BSTNode(T v) { value = v; }
	};

public:
	BinarySearchTree() {};

	InsertionInfo insert(T v) {
		return insert(v, root);
	}

	void print() {
		print_tree(root);
	}

	SearchInfo search(T v) {}

private:

	std::unique_ptr<BSTNode> root;

	InsertionInfo insert(T v, std::unique_ptr<BSTNode>& node) {

		if (!node) {
			node = std::make_unique<BSTNode>(v);
			return InsertionInfo::Inserted;
		}
		else if (v == node->value) {
			return InsertionInfo::AlreadyIn;
		}
		else {
			return (v > node->value) ? insert(v, node->right) : insert(v, node->left);
		}
	}

	void print_tree(std::unique_ptr<BSTNode>& node) {
		if (!node) {
			return;
		}

		print_tree(node->left);
		std::cout << node->value << "\t";
		print_tree(node->right);
	}
};