#include <vector>
#include <list>
#include "Util.h"
#include "Sorting.h"
#include "Student.cpp" 
#include "Search.h"
#include "ClosestPair.h"
#include "BinarySearchTree.cpp"

int main() {

	BinarySearchTree<int> bt;

	bt.insert(5);
	bt.insert(3);
	bt.insert(8);
	bt.insert(18);
	bt.insert(2);
	bt.insert(1);

	bt.print();
}
