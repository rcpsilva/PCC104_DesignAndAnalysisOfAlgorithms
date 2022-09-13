#include <vector>
#include <list>
#include "Util.h"
#include "Sorting.h"
#include "Student.cpp" 

int main() {
	std::vector<int> v({0,0,0,5,4,3});
	printSequence(v);
	selection_sort(v);
	printSequence(v);

	
	std::list<Student> l({});
	l.push_back(Student("Rodrigo", 8));
	l.push_back(Student("Joao", 1));
	l.push_back(Student("Antonio", 10));
	printSequence(l);
	
	selection_sort(l.begin(), l.end());
	printSequence(l);
	
	selection_sort(l.begin(), l.end(), compStudentsName());
	printSequence(l);

	selection_sort(l.begin(), l.end(), compStudentsGrade());
	printSequence(l);

}
