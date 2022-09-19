#include <vector>
#include <list>
#include "Util.h"
#include "Sorting.h"
#include "Student.cpp" 
#include "Search.h"

int main() {
	
	printf("All \n");
	generate_permutations(4);

	/*printf("Combinations \n");
	generate_combinations(3);

	printf("Permutations \n");
	generate_permutations(3);

	printf("TSP \n");
	std::vector<std::vector<int>> costs({
		{0,80,50},
		{0,0,40},
		{12,10,0} });
	
	printSequence(tsp_brute_force(costs));*/
}
