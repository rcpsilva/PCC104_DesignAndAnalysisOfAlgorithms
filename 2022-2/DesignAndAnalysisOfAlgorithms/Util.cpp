#include <iostream>

template<class Iterable> void printSequence(Iterable sequence) {
	for (auto e : sequence) {
		std::cout << e << " ";
	}
	std::cout << std::endl;
}

template<class Iterable> void printSequenceSequence(Iterable sequence) {
	for (auto e : sequence) {
		printSequence(e);
	}
}