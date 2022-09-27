#include<vector>
#include<cmath>
#include"FakeCoin.h"

int weight(std::vector<int>& v, int begin, int end) {

	int w = 0;
	for (int i = begin; i < end; i++)
	{
		w += v[i];
	}
	return w;
}

int fake_coin(std::vector<int>& v, int begin, int end) {

	if (end - begin == 1) {
		return begin;
	}
	else {

		int midpoint = std::floor((float)(begin + end) / 2);

		int w1 = weight(v, begin, midpoint);
		int w2 = weight(v, midpoint, end);

		if (w1 < w2) {
			return fake_coin(v, begin, midpoint);
		}
		else {
			return fake_coin(v, midpoint, end);
		}

	}

}

int fake_coin(std::vector<int>& v) {

	return fake_coin(v, 0, v.size());

}