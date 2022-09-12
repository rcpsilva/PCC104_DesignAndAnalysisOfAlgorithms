#include <vector>
#include <queue>
#include <list>
#include <chrono>
#include <iostream>
#include <cstdio>
#include "Sorting.h"

int main() {

	std::vector<int> grid = { 5,3,0,0,7,0,0,0,0 };

	// selection_sort(grid);

	selection_sort(grid.begin(), grid.end());

	for (auto s : grid) {
		std::printf(" %d ", s);
	}
}
