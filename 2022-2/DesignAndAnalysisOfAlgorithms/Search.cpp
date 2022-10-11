#include <vector>
#include <algorithm>
#include <limits>
#include <numeric>
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


void johnsonTrotter(int n) {
	int count = 0;

	std::vector<int> v(n);
	std::iota(v.begin(), v.end(), 1);

	std::vector<int> directions(n,-1); //-1 = <- ; 1 = ->

	int there_is_mobile = true;

	std::cout << count << std::endl;
	printSequence(v);

	while (there_is_mobile){

		there_is_mobile = false;

		//Find largest mobile element
		int mobile = -1;
		int idx_mobile = -1;
		int neighbor = 0;
		
		for (int i = 0; i < v.size(); i++)
		{
			if ( (i + directions[i] < n) && (i + directions[i] >= 0) ) {
				if ((v[i] > mobile) && (v[i + directions[i]] < v[i])) {
					mobile = v[i];
					idx_mobile = i;
					neighbor = directions[i];
					there_is_mobile = true;
				}
			}
			
		}

		
		if (there_is_mobile) {
			// swap k with the adjacent element k’s arrow points to	
			std::swap(v[idx_mobile], v[idx_mobile + neighbor]);
			std::swap(directions[idx_mobile], directions[idx_mobile + neighbor]);

			// reverse the direction of all the elements that are larger than k

			for (int i = 0; i < v.size(); i++)
			{
				if (v[i] > mobile) {
					directions[i] = directions[i] * (-1);
				}
			}

			count += 1;
			std::cout << count << std::endl;
			printSequence(v);
		}
		
	}
}