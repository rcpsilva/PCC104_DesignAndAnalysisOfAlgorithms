#include <vector>
#include <algorithm>
#include <iterator>

template <typename T> void selection_sort(std::vector<T>& v)
{
	int min;

	for (int i = 0; i < v.size(); i++) {
		min = i;
		for (int j = i + 1; j < v.size(); j++) {
			if (v[j] < v[min]) {
				min = j;
			}
		}
		std::swap(v[i], v[min]);
	}

}

template<class It, class C> void selection_sort(It first, It last, C comparator) {

	for (auto it = first; it != last; ++it) {
		iter_swap(it, std::min_element(it, last, comparator));
	}
}

template<class It> void selection_sort(It first, It last) {

	selection_sort(first, last, std::less<std::decay_t<decltype(*first)>>());
}