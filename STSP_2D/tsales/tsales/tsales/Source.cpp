#include <iostream>
#include <map>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <algorithm>

// mini_map = {
// 	"AA": {"x": 0, "y": 13},
// 	"AB": {"x": 0, "y": 26},
// 	"AC": {"x": 0, "y": 27},
// 	"AD": {"x": 0, "y": 39},
// 	"AE": {"x": 2, "y": 0},
// 	"AF": {"x": 5, "y": 13},
// 	"AG": {"x": 5, "y": 19},
// 	"AH": {"x": 5, "y": 25},
// 	"AI": {"x": 5, "y": 31},
// 	"AJ": {"x": 5, "y": 37}
// }

using namespace std;

// PRINTING FUNCTIONS
	void print_vector(vector<string> vec);
	void print_path(vector<string> path);
	void print_path_and_values(vector<string> path, map<string, vector<int> > mapa);
	void print_array_of_paths(vector<vector<string>> path_array);
	void print_array_of_paths_and_values(vector<vector<string>> path_array, map<string, vector<int> > mapa);

// DISTANCE CALCULATION
	double get_distance(string s1, string s2, map<string, vector<int> > mapa);
	double get_path_length(vector<string> nodes, map<string, vector<int> > mapa);
	double get_path_length(vector<string> nodes, map<string, vector<int> > mapa);

// COMPARE FUNCTIONS
	bool compare_two(vector<string> v1, vector<string> v2);
	bool check_for_cycles(vector<string> path);

// COLLECTION FUNCTIONS
	map<string, vector<int>> build_data_map();
	vector<string> get_nodes(map<string, vector<int> > mapa);
	vector<vector<string>> create_initial_population(map<string, vector<int>> mapa, unsigned int population_size);
	
// UTILITIES
	vector<string> shuffle(vector<string> nodes);
	vector<string> find_best_path(vector<vector<string>> population, map<string, vector<int> > mapa, unsigned int worst_possible_path_lenght);
	vector<vector<string>> pick_better_half(vector<vector<string>> population, map<string, vector<int> > mapa, unsigned int worst_possible_path_lenght);



int main(){
	// VARIABLES
	unsigned int population_size = 30;
	double mutation_threshold = 0.021;
	unsigned int iteration_threshold = 100;
	unsigned int worst_possible_path_lenght = UINT_MAX;

	// BUILDING DATA MAP
	map<string, vector<int> > mapa = build_data_map();

	// CREATING INITIAL POPULATION
	vector<vector<string>> population_1 = create_initial_population(mapa, population_size);

	// SHOW INITIAL POPULATION
	print_array_of_paths_and_values(population_1, mapa);

	// FIND BEST PATH
	vector<string> best_path = find_best_path(population_1, mapa, worst_possible_path_lenght);
	
	  // BEGIN
	 //
	// GET BETTER HALF OF POPULATION
	vector<vector<string>> better_half = pick_better_half(population_1, mapa, worst_possible_path_lenght);
	cout << endl;
	print_array_of_paths_and_values(better_half, mapa);

		// CREATING NEXT POPULATION

			// PICKING TWO FROM BETTER HALF

			// CROSSOVER

			// MUTATION

			// CHECK CHILDREN FOR CYCLES

			// CHECK IF CHILDREN DO NOT HAVE DUPLICATES IN NEXT POPULATION

		// IF NEW BEST PATH IS BETTER THEN CURRENT RECORD HOLDER

		// SET NEXT POPULATION AS CURRENT ONE 

	// EPILOG
	system("PAUSE");
	return 0;
}






vector<vector<string>> pick_better_half(vector<vector<string>> population, map<string, vector<int> > mapa, unsigned int worst_possible_path_lenght){
	// GETTING BETTER HALF
	vector<vector<string>> better_half;
	vector<vector<string>> local_population = population;

	for (unsigned int i = 0; i < population.size()/2; ++i){
		vector<string> best_one = find_best_path(local_population, mapa, worst_possible_path_lenght);
		better_half.push_back(best_one);
		for (unsigned int j = 0; j < local_population.size(); ++j){
			if (best_one == local_population.at(j)){
				local_population.erase(std::remove(local_population.begin(), local_population.end(), best_one), local_population.end());
			}
		}
	}
	return better_half;
}









vector<string> find_best_path(vector<vector<string>> population, map<string, vector<int> > mapa, unsigned int worst_possible_path_lenght){
	// FINDS BEST SOLUTION IN POPULATION
	vector <string> best_path;
	double best_path_length = worst_possible_path_lenght;
	for (unsigned int i = 0; i < population.size(); ++i){
		double length = get_path_length(population.at(i), mapa);
		if (length < best_path_length){
			best_path_length = length;
			best_path = population.at(i);
		}
	}
	return best_path;
}

bool check_for_cycles(vector<string> path){
	// CHECKS FOR CYCLES IN PATH
	for (unsigned int i = 0; i < path.size(); ++i){
		int check = 0;
		for (unsigned int j = 0; j < path.size(); ++j){
			if (path.at(i) == path.at(j)){
				++check;
			}
		}
		if (check > 1){
			return false;
		}
	}
	return true;
}

vector<string> get_nodes(map<string, vector<int> > mapa){
	// GETS ALL NODE NAMES FROM MAP AND STORES IN A STRING VECTOR
	vector<string> result;
	for (map<string, vector<int> >::iterator it = mapa.begin(); it != mapa.end(); ++it){
		result.push_back(it->first);
	}
	return result;
}

double get_distance(string s1, string s2, map<string, vector<int> > mapa){
	// GETS EUCLIDESIAN DISTANCE BETWEEN TWO POINS IN A PLANE
	int x1 = mapa[s1].at(0);
	int y1 = mapa[s1].at(1);
	int x2 = mapa[s2].at(0);
	int y2 = mapa[s2].at(1);
	//cout << "Calculating for " << x1 << "," << y1 << "," << x2 << "," << y2 << endl;
	return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

void print_vector(vector<string> vec){
	// PRINTS VECTOR
	for (unsigned int i = 0; i < vec.size(); ++i){
		cout << "[" << i << "] = " << vec.at(i) << endl;
	}
}

void print_path(vector<string> path){
	// PRINTS PATH
	for (unsigned int i = 0; i < path.size(); ++i){
		cout << "[" << path.at(i) << "] ";
	}
	cout << endl;
}

void print_path_and_values(vector<string> path, map<string, vector<int> > mapa){
	// PRINTS PATH
	for (unsigned int i = 0; i < path.size(); ++i){
		cout << "[" << path.at(i) << "] ";
	}
	cout << "\t" << get_path_length(path, mapa);
	cout << endl;
}

void print_array_of_paths(vector<vector<string>> path_array){
	// PRINTS MULTIPLE PATHS
	for (unsigned int i = 0; i < path_array.size(); ++i){
		print_path(path_array.at(i));
	}
}

void print_array_of_paths_and_values(vector<vector<string>> path_array, map<string, vector<int> > mapa){
	// PRINTS MULTIPLE PATHS
	for (unsigned int i = 0; i < path_array.size(); ++i){
		print_path_and_values(path_array.at(i), mapa);
	}
}

double get_path_length(vector<string> nodes, map<string, vector<int> > mapa){
	// GETS LENGTH OF A GIVEN PATH
	double sum = 0;
	for (unsigned int i = 0; i < nodes.size()-1; ++i){
		sum += get_distance(nodes.at(i), nodes.at(i + 1), mapa);
	}
	return sum;
}

vector<string> shuffle(vector<string> nodes){
	// REORDERING NODES IN PATH
	random_shuffle(nodes.begin(), nodes.end());
	return nodes;
}

bool compare_two(vector<string> v1, vector<string> v2){
	// COMPARES TWO PATHS
	for (unsigned int i = 0; i < v1.size(); ++i){
		if (v1.at(i) != v2.at(i)){
			return false; // DIFFERENT
		}
	}
	return true; // THE SAME
}

vector< vector<string> > create_initial_population(map<string, vector<int> > mapa, unsigned int population_size){
	// CREATES INITIAL POPULATION
	vector<vector<string>> population;
	vector<string> adam = get_nodes(mapa);

	while (population.size() < population_size){
		vector<string> being = shuffle(adam);
		if (population.size() < 1){
			population.push_back(being);
		}
		else {
			unsigned int check = 0;
			for (unsigned int i = 0; i < population.size(); ++i){
				if (compare_two(being, population.at(i))){
					++check;
				}
			}
			if (check == 0){
				population.push_back(being);
			}
		}
	}
	return population;
}

map<string, vector<int> > build_data_map(){

	vector<int> point;
	map<string, vector<int> > mapa;

	point.push_back(0);
	point.push_back(13);
	mapa["AA"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(26);
	mapa["AB"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(27);
	mapa["AC"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(39);
	mapa["AD"] = point;
	point.clear();

	point.push_back(2);
	point.push_back(0);
	mapa["AE"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(13);
	mapa["AF"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(19);
	mapa["AG"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(25);
	mapa["AH"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(31);
	mapa["AI"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(37);
	mapa["AJ"] = point;
	point.clear();

	return mapa;
}