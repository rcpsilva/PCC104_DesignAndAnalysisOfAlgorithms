#include <vector>
#include <algorithm>
#include <limits>
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

void generate_permutations(std::vector<int>& solution, int n) {

	if (goal(solution, n)) {
		printSequence(solution);
	}
	else {
		for (int i = 1; i <= n; i++)
		{
			if (std::find(solution.begin(), solution.end(), i) == solution.end()) {
				solution.push_back(i);
				generate_permutations(solution, n);
				solution.pop_back();
			}
		}
	}
}

void generate_permutations(int n) {

	std::vector<int> solution({});
	generate_permutations(solution, n);
}


void tsp_brute_force(std::vector<int>& solution, int n, std::vector<std::vector<int>>& costs, int best_val, std::vector<int>& best_sol) {

	if (goal(solution, n)) {
		int cost = 0;
		for (size_t i = 0; i < n; i++)
		{
			cost += costs[solution[i] - 1][solution[(i + 1) % n] - 1];
		}
		if (cost < best_val) {
			best_val = cost;
			best_sol.assign(solution.begin(), solution.end());
		}

		printf("Cost %d \n", cost);
		printSequence(solution);
		printf("\n");
	}
	else {
		for (int i = 1; i <= n; i++)
		{
			if (std::find(solution.begin(), solution.end(), i) == solution.end()) {
				solution.push_back(i);
				tsp_brute_force(solution, n, costs, best_val, best_sol);
				solution.pop_back();
			}
		}
	}
}

std::vector<int> tsp_brute_force(std::vector<std::vector<int>>& costs) {

	std::vector<int> solution({});
	std::vector<int> best_sol({});
	tsp_brute_force(solution, costs.size(), costs, std::numeric_limits<int>::max(), best_sol);
	return best_sol;

}
