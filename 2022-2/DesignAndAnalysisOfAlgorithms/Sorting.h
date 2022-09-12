#pragma once

template <typename T> void selection_sort(std::vector<T>&);

template <class It, class C> void selection_sort(It, It, C);

template <class It> void selection_sort(It, It);

#include "Sorting.cpp"