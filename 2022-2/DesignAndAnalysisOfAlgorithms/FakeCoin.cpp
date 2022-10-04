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
	else if (end - begin == 2) {
		return v[begin] < v[begin + 1] ? begin : begin + 1;
	}
	else {

		int pile_size = std::floor((float)(end - begin) / 3);

		int w1 = weight(v, begin, begin + pile_size);
		int w2 = weight(v, begin + pile_size, begin + 2 * pile_size);
		int w3 = weight(v, begin + 2 * pile_size, end);


		if (w1 == w2) {
			return fake_coin(v, begin + 2 * pile_size, end);
		}
		else if (w2 < w1) {
			return fake_coin(v, begin + pile_size, begin + 2 * pile_size);
		}
		else {
			return fake_coin(v, begin, begin + pile_size);
		}

	}

}

int fake_coin(std::vector<int>& v) {

	return fake_coin(v, 0, v.size());

}