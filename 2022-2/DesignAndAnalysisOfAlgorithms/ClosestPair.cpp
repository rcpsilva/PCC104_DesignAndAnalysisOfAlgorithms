#include <vector>
#include <cmath>
#include <limits>

template<typename T> std::vector<std::vector<T>> closet_pair(std::vector<std::vector<T>> points) {

	std::vector<std::vector<T>> closest_pair({ {0,0},{0,0} });
	T min_dist = std::numeric_limits<T>::max();

	for (size_t i = 0; i < points.size() - 1; i++)
	{
		for (size_t j = i + 1; j < points.size(); j++)
		{
			T dist = std::sqrt(std::pow(points[i][0] - points[j][0], 2) + std::pow(points[i][1] - points[j][1], 2));

			if (dist < min_dist) {
				min_dist = dist;
				closest_pair[0] = points[i];
				closest_pair[1] = points[j];

			}

		}
	}

	return closest_pair;
}