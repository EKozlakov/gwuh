openmp1: openmp1.cpp
	g++ -g -Wall -fopenmp -std=c++11 -o $@ $<

openmp2: openmp2.cpp
g++ -g -Wall -fopenmp -std=c++11 -o $@ $<