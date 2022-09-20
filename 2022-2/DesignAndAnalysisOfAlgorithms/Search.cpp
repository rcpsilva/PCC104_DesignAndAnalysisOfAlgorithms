#include <vector>
#include <algorithm>
#include <limits>
#include "Util.h"


std::vector<int> solve_tsp(std::vector<std::vector<int>>& costs, std::vector<int> solution, int& best_cost, std::vector<int>& best_solution) {

	if (solution.size() == costs.size()) {
		int cost = 0;
		for (int i = 0; i < costs.size(); i++)
		{
			cost += costs[solution[i]][solution[(i + 1) % costs.size()]];
		}

		printf("Cost %d :", cost);
		printSequence(solution);

		if (cost < best_cost) {
			best_cost = cost;
			best_solution.assign(solution.begin(), solution.end());
		}

	}
	else {

		for (int i = 0; i < costs.size(); i++)
		{
			if (std::find(solution.begin(), solution.end(), i) == solution.end()) {
				solution.push_back(i);
				solve_tsp(costs, solution, best_cost, best_solution);
				solution.pop_back();
			}
		}

	}

	return best_solution;

	
}

std::vector<int> solve_tsp(std::vector<std::vector<int>>& costs) {
	
	std::vector<int> solution({});
	std::vector<int> best_solution({});
	int max = std::numeric_limits<int>::max();
	int& best_ref = max;
	solve_tsp(costs, solution, best_ref, best_solution);
	return best_solution;
}

void generate_permutations(int n, std::vector<int>& solution) {
	
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

void generate_subsets(int n, std::vector<int>& solution, int start_from) {

	printSequence(solution);
	if (solution.size() == n) {
		return;
	}
	else {
		for (int i = start_from; i < n; i++)
		{
			if (std::find(solution.begin(), solution.end(), i) == solution.end()) {
				solution.push_back(i);
				generate_subsets(n, solution, i+1);
				solution.pop_back();
			}
		}
	}
}

void generate_subsets(int n) {
	
	std::vector<int> solution({});
	generate_subsets(n, solution, 0);
}


void generate_binarysets(int n, std::vector<int>& solution) {

	
	if (solution.size() == n) {
		printSequence(solution);
		return;
	}
	else {
		for (int i = 0; i <= 1; i++)
		{
			solution.push_back(i);
			generate_binarysets(n, solution);
			solution.pop_back();
		}
	}
}

void generate_binarysets(int n) {

	std::vector<int> solution({});
	generate_binarysets(n, solution);
}

