#include <vector>
#include <list>
#include "Util.h"
#include "Sorting.h"
#include "Student.cpp" 
#include "Search.h"
#include "ClosestPair.h"
#include "BinarySearchTree.cpp"
#include "BinarySearch.h"

int main() {

	BinarySearchTree<int> bt;

	bt.insert(5);
	bt.insert(3);
	bt.insert(8);
	bt.insert(18);
	bt.insert(2);
	bt.insert(1);

	bt.print();

	std::cout << "\nBinary Search" << std::endl;

	std::vector<int> v({ 1,2,3,6,8,10,19});

	std::cout << binary_search(v,19) << std::endl;
}
