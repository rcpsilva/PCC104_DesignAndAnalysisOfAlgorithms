#include <vector>
#include <list>
#include "Util.h"
#include "Sorting.h"
#include "Student.cpp" 
#include "Search.h"
#include "ClosestPair.h"

int main() {

	std::vector<std::vector<float>> points({ {3,3},
		{14,1},
		{4,6},
		{8,9},
		{12,123},
		{2,5},
		{3.1,3.2},
		{7,8}, });

	printf("Closest Pair \n");
	printSequenceSequence(closet_pair<float>(points));


	printf("All \n");
	generate_permutations(4);

	printf("Combinations \n");
	generate_subsets(4);

	printf("Binary strings \n");
	generate_binarysets(4);

	printf("Subsets \n");
	generate_subsets(4);


	printf("TSP \n");
	std::vector<std::vector<int>> costs({
		{0,10,50,15},
		{9,0,20,15},
		{8,11,0,12},
		{23,15,10,0}});
	
	printSequence(solve_tsp(costs));
}
