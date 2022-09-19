#include <vector>
#include <algorithm>
#include "Util.h"

void generate_permutations(int n, std::vector<int> solution) {
	
	if (solution.size() == n) {
		printSequence(solution);
	}
	else {
		for (int i = 0; i < n; i++)
		{
			if (std::find(solution.begin(), solution.end(), i) == solution.end()) {
				solution.push_back(i);
				generate_permutations(n,solution);
				solution.pop_back();
			}
		}
	}
}

void generate_permutations(int n) {
	std::vector<int> solution({});
	generate_permutations(n, solution);
}