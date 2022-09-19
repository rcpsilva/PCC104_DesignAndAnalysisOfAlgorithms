#include <vector>
#include <algorithm>
#include "Util.h"
#include "Search.h"

bool goal(std::vector<int> solution, int n) {
	return (solution.size() == n);
}
	
void generate_all_vals(std::vector<int>& solution, int n) {

	if (goal(solution, n)) {
		printSequence(solution);
	}
	else {
		for (int i = 1; i <= n ; i++)
		{
			solution.push_back(i);
			generate_all_vals(solution,n);
			solution.pop_back();
		}
	}
}

void generate_all_vals(int n) {

	std::vector<int> solution({});
	generate_all_vals(solution, n);
}


void generate_combinations(std::vector<int>& solution, int n) {

	printSequence(solution);
	if (solution.size() == n) {
		return;
	}
	else {
		for (int i = 1; i <= n; i++)
		{
			solution.push_back(i);
			generate_combinations(solution, n);
			solution.pop_back();
		}
	}
	
}

void generate_combinations(int n) {

	std::vector<int> solution({});
	generate_combinations(solution, n);
}

void generate_permutations1(std::vector<int>& solution, int n) {

	if (goal(solution, n)) {
		printSequence(solution);
	}
	else {
		for (int i = 1; i <= n; i++)
		{
			if (std::find(solution.begin(), solution.end(), i) == solution.end()) {
				solution.push_back(i);
				generate_permutations1(solution, n);
				solution.pop_back();
			}
		}
	}
}

void generate_permutations(int n) {

	std::vector<int> solution({});
	generate_permutations1(solution, n);
}
