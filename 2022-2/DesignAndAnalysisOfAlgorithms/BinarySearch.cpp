#include<vector>
#include<cmath>
#include"BinarySearch.h"

int binary_search(std::vector<int>& v, int key, int begin, int end) {

	if (end - begin == 0) {
		return -1;
	}
	else {

		int midpoint = std::floor((float)(begin + end) / 2);

		if (key == v[midpoint]) {
			return midpoint;
		}
		else {
			return (key < v[midpoint]) ? binary_search(v, key, begin, midpoint) : binary_search(v, key, midpoint + 1, end);
		}

	}

}

int binary_search(std::vector<int>& v, int key) {

	return binary_search(v, key, 0, v.size());

}