#include <iostream>
#include <map>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <climits>
#include <stdlib.h>
#include <time.h>
#include <ctime>

int DEBUG = 0;

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
	bool contains_cycles(vector<string> path);

// COLLECTION FUNCTIONS
	map<string, vector<int>> build_data_map();
	vector<string> get_nodes(map<string, vector<int> > mapa);
	vector<vector<string>> create_initial_population(map<string, vector<int>> mapa, unsigned int population_size);
	
// UTILITIES
	vector<string> shuffle(vector<string> nodes);
	vector<string> find_best_path(vector<vector<string>> population, map<string, vector<int> > mapa, unsigned int worst_possible_path_lenght);
	vector<vector<string>> pick_better_half(vector<vector<string>> population, map<string, vector<int> > mapa, unsigned int worst_possible_path_lenght);
	int get_random_num(int mod);
	vector<vector<string>> pick_two(vector<vector<string>> population);
	vector<vector<string>> crossover(vector<vector<string>> parents, map<string, vector<int> > mapa);
	vector<vector<string>> mutation(vector<vector<string>> children, map<string, vector<int> > mapa);
	void solve(vector<vector<string>> population_1, map<string, vector<int> > mapa, int iterations);

int main(){

	// VARIABLES
	unsigned int population_size = 30;
	double mutation_threshold = 0.021;
	unsigned int iteration_threshold = 100;
	unsigned int worst_possible_path_lenght = UINT_MAX;

	srand(time(NULL));
	

	// BUILDING DATA MAP
	map<string, vector<int> > mapa = build_data_map();
	population_size = mapa.size();



	// CREATING INITIAL POPULATION
	clock_t begin = clock();
	vector<vector<string>> population_1 = create_initial_population(mapa, population_size);
	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << "Time spent on creating initial population: " << elapsed_secs << endl; 

	solve(population_1, mapa, 100);

	return 0;
	
}



void solve(vector<vector<string>> population_1, map<string, vector<int> > mapa, int iterations){

	double best_path_length = UINT_MAX;
	vector<string> best_path;
	unsigned int best_path_reached_in_iteration = 0;
	unsigned int iteration_counter = 0;
	vector<vector<string>> local_population = population_1;

	while ( iterations > 0 ){
		clock_t begin_iteration = clock();
		vector<vector<string>> next_population;
		clock_t begin_better_half = clock();
		vector<vector<string>> better_half = pick_better_half(local_population, mapa, UINT_MAX);
		clock_t end_better_half = clock();
		cout << "Time spent on picking better half " << double(end_better_half - begin_better_half) / CLOCKS_PER_SEC << endl;

		while (next_population.size() < population_1.size()){

			clock_t begin_pt = clock();
			vector<vector<string>> parents = pick_two(better_half);
			clock_t end_pt = clock();
			cout << "Time spent on picking parents " << double(end_pt - begin_pt) / CLOCKS_PER_SEC << endl;

			if (DEBUG == 1) cout << "\nPARENTS:" << endl;
			if (DEBUG == 1) print_array_of_paths(parents);

			vector<vector<string>> children = crossover(parents, mapa);
			children = mutation(children, mapa);

			bool cycles_in_daughter = contains_cycles(children.at(0));
			bool cycles_in_son = contains_cycles(children.at(1));
			bool check_identical = compare_two(children.at(0), children.at(1));

			if ( check_identical == false ){
				if ( next_population.size() < 1 ){
					if (!cycles_in_daughter) next_population.push_back(children.at(0));
					if (!cycles_in_son) next_population.push_back(children.at(1));
				}
				else {
					int daughter_check = 0;
					int son_check = 0;
					for (unsigned int i = 0;  i < next_population.size(); ++i){
						if (children.at(0) == next_population.at(i)) ++daughter_check;
						if (children.at(1) == next_population.at(i)) ++son_check;
					}
					if (daughter_check < 1 && !cycles_in_daughter) next_population.push_back(children.at(0));
					if (son_check < 1 && !cycles_in_son) next_population.push_back(children.at(1));
				}
			} 
		}
		clock_t end_iteration = clock();
		double iteration_elapsed_secs = double(end_iteration - begin_iteration) / CLOCKS_PER_SEC;
		cout << "Time spent on iteration " << iteration_elapsed_secs << endl; 

		// PICK BEST PATH
		vector<string> local_best_path =  find_best_path(next_population, mapa, UINT_MAX);
		double local_best_path_length = get_path_length(local_best_path, mapa);
		cout << "Iteration " << iteration_counter+1 << ". Best path length: " << local_best_path_length << endl;
		if (local_best_path_length < best_path_length) {
			best_path_length = local_best_path_length;
			best_path = local_best_path;
		}
		local_population = next_population;
		++iteration_counter;
		--iterations;
	}
	cout << "Best path length: " << best_path_length << " reached in " << iteration_counter << " iteration." << endl;

}



vector<vector<string>> mutation(vector<vector<string>> children, map<string, vector<int> > mapa){
	if (DEBUG == 1) cout << "In mutation" << endl;
	if ( get_random_num(1000) > 21 ){
	//if ( get_random_num(20) > 21 ){
		if (DEBUG == 1) cout << "No mutation" << endl;
		return children;
	} 

	if (DEBUG == 1) print_array_of_paths(children);
	vector<vector<string>> mutated_children;

	if (DEBUG == 1) cout << "1" << endl;
	vector<string> daughter = children.at(0);
	if (DEBUG == 1) cout << "2" << endl;
	vector<string> son = children.at(1);
	if (DEBUG == 1) cout << "3" << endl;

	if (DEBUG == 1) cout << "Searching for mutation points" << endl;
	// CHOOSE MUTATION POINTS
	int mutation_point_1 = get_random_num( (children.at(0)).size() );
	int mutation_point_2 = get_random_num( (children.at(0)).size() );
	while ( mutation_point_1 == mutation_point_2){
		mutation_point_2 = get_random_num( (children.at(0)).size() );
	}

	if (DEBUG == 1) cout << "Mutation " << mutation_point_1 << " Mutation " << mutation_point_2 << endl;

	// GET CROSSING POINTS IN ORDER
	int smaller = (mutation_point_1 < mutation_point_2)?(mutation_point_1):(mutation_point_2);
	int bigger = (mutation_point_1 < mutation_point_2)?(mutation_point_2):(mutation_point_1);

	if (DEBUG == 1) cout << smaller << " < " << bigger << endl;

	// COLLECTING SUBPATH FOR MUTATION
	vector<string> daughter_mutation;
	vector<string> son_mutation;
	for (unsigned int i = smaller; i < bigger; ++i){
		daughter_mutation.push_back(daughter.at(i));
		son_mutation.push_back(son.at(i));
	}
	if (DEBUG == 1) cout << "Before reversal:" << endl;
	if (DEBUG == 1) print_path(daughter_mutation);
	if (DEBUG == 1) print_path(son_mutation);
	reverse(daughter_mutation.begin(), daughter_mutation.end());
	reverse(son_mutation.begin(), son_mutation.end());
	if (DEBUG == 1) cout << "After reversal:" << endl;
	if (DEBUG == 1) print_path(daughter_mutation);
	if (DEBUG == 1) print_path(son_mutation);

	// MUTATING
	unsigned int index = 0;
	for (unsigned int i = smaller; i < bigger; ++i){
		daughter[i] = daughter_mutation.at(index);
		son[i] = son_mutation.at(index);
		++index;
	}

	if (DEBUG == 1) cout << "After mutation:" << endl;
	if (DEBUG == 1) print_path(daughter);
	if (DEBUG == 1) print_path(son);

	mutated_children.push_back(daughter);
	mutated_children.push_back(son);

	return mutated_children;
}


vector<vector<string>> crossover(vector<vector<string>> parents, map<string, vector<int> > mapa){
	// CREATES DESCENDANTS
	vector<vector<string>> children;

	// CHECK WHETHER PARENTS LIKE EACH OTHER ENOUGH
	if ( get_random_num(100) > 70 ) return parents;

	if (DEBUG == 1) cout << "Attempting crossing" << endl;
	// CHOOSE CROSSING POINTS
	int crossing_point_1 = get_random_num( (parents.at(0)).size() );
	int crossing_point_2 = get_random_num( (parents.at(0)).size() );
	while ( crossing_point_1 == crossing_point_2){
		crossing_point_2 = get_random_num( (parents.at(0)).size() );
	}

	if (DEBUG == 1) cout << "Cross " << crossing_point_1 << " Cross " << crossing_point_2 << endl;
	// GET CROSSING POINTS IN ORDER
	int smaller = (crossing_point_1 < crossing_point_2)?(crossing_point_1):(crossing_point_2);
	int bigger = (crossing_point_1 < crossing_point_2)?(crossing_point_2):(crossing_point_1);

	if (DEBUG == 1) cout << smaller << " < " << bigger << endl;

	vector<string> daughter;
	vector<string> son;

	if (DEBUG == 1) cout << "Mothers gene size: " << parents.at(0).size() << endl;
	// FILLING CHILDREN WITH EMPTY GENES
	for (unsigned int i = 0; i < (parents.at(0)).size(); ++i ){
		if (DEBUG == 1) cout << "Filling children " << i << endl; 
		daughter.push_back(" ");
		son.push_back(" ");
	}
	if (DEBUG == 1) cout << "After zero filling:" << endl;

	if (DEBUG == 1) print_path(daughter);
	if (DEBUG == 1) print_path(son);

	if (DEBUG == 1) cout << "After cross filling: " << endl;

	// FILLING CHILDREN WITH PARENT GENES BETWEEN CROSSING POINTS
	// SON GETS GENES FROM MOTHER, DAUGHTER FROM FATHER
	// COLLECTING DATA FOR RULES CREATION
	vector<string> mother_data;
	vector<string> father_data;
	for (unsigned int i = smaller; i < bigger; ++i){
		daughter[i] = (parents.at(1)).at(i);
		mother_data.push_back((parents.at(1)).at(i));

		son[i] = (parents.at(0)).at(i);
		father_data.push_back((parents.at(0)).at(i));
	}
	if (DEBUG == 1)print_path(daughter);
	if (DEBUG == 1)print_path(son);

	// CREATE RULES FROM PARENTS
	vector<vector<string>> rules;
	for (unsigned int i = 0; i < mother_data.size(); ++i){
		vector<string> rule_1;
		vector<string> rule_2;
		rule_1.push_back(mother_data.at(i));
		rule_1.push_back(father_data.at(i));
		rule_2.push_back(father_data.at(i));
		rule_2.push_back(mother_data.at(i));
		
		rules.push_back(rule_1);
		rules.push_back(rule_2);
	}
	if (DEBUG == 1) cout << "Rules:" << endl;
	if (DEBUG == 1) print_array_of_paths(rules);

	// FILLING CHILDREN EMPTY GENES 1
	for (unsigned int i = 0; i < smaller; ++i){
		for (unsigned int j = 0; j < rules.size(); ++j){
			if ( (rules.at(j)).at(0) == (parents.at(0)).at(i) ){
				daughter[i] = (rules.at(j)).at(1);
			}
			if ( (rules.at(j)).at(0) == (parents.at(1)).at(i) ){
				son[i] = (rules.at(j)).at(1);
			}
		}
	}

	if (DEBUG == 1) cout << "After filling sub gene 1:" << endl;
	if (DEBUG == 1) print_path(parents.at(0));
	if (DEBUG == 1) print_path(daughter);
	if (DEBUG == 1) cout << endl;
	if (DEBUG == 1) print_path(parents.at(1));
	if (DEBUG == 1) print_path(son);

	// FILLING CHILDREN EMPTY GENES 1
	for (unsigned int i = bigger; i < daughter.size(); ++i){
		for (unsigned int j = 0; j < rules.size(); ++j){
			if ( (rules.at(j)).at(0) == (parents.at(0)).at(i) ){
				daughter[i] = (rules.at(j)).at(1);
			}
			if ( (rules.at(j)).at(0) == (parents.at(1)).at(i) ){
				son[i] = (rules.at(j)).at(1);
			}
		}
	}

	if (DEBUG == 1) cout << "After filling sub gene 2:" << endl;
	if (DEBUG == 1) print_path(parents.at(0));
	if (DEBUG == 1) print_path(daughter);
	if (DEBUG == 1) cout << endl;
	if (DEBUG == 1) print_path(parents.at(1));
	if (DEBUG == 1) print_path(son);

	// COLLECTING UNUSED GENES FROM MOMMY
	vector<string> unused_mommy_genes;
	vector<string> unused_daddy_genes;
	for (unsigned int i = 0; i < daughter.size(); ++i){
		if (daughter.at(i) == " ") unused_mommy_genes.push_back( (parents.at(0)).at(i) ); 
	}
	for (unsigned int i = 0; i < son.size(); ++i){
		if (son.at(i) == " ") unused_daddy_genes.push_back( (parents.at(1)).at(i) ); 
	}

	if (DEBUG == 1)cout << "Remaing genes:" << endl;
	if (DEBUG == 1)print_path(unused_mommy_genes);
	if (DEBUG == 1)print_path(unused_daddy_genes);

	// FILLING REMAINING EMPTY GENES IN CHILDREN
	unsigned int index = 0;
	for (unsigned int i = 0; i < daughter.size(); ++i){
		if (daughter.at(i) == " "){
			daughter[i] = unused_daddy_genes.at(index);
			++index;
		}
	}
	index = 0;
	for (unsigned int i = 0; i < son.size(); ++i){
		if (son.at(i) == " "){
			son[i] = unused_mommy_genes.at(index);
			++index;
		}
	}

	if (DEBUG == 1) cout << "After full crossing:" << endl;
	if (DEBUG == 1) print_path(parents.at(0));
	if (DEBUG == 1) print_path(daughter);
	if (DEBUG == 1) cout << endl;
	if (DEBUG == 1) print_path(parents.at(1));
	if (DEBUG == 1) print_path(son);	
	children.push_back(daughter);
	children.push_back(son);
	return children;
}

vector<vector<string>> pick_two(vector<vector<string>> population)
{
	

			
	int counter = 0;		

	vector<vector<string>> pair;
	while (pair.size() != 2){
		clock_t begin_pt = clock();
		unsigned int random = get_random_num( population.size() );
		clock_t end_pt = clock();
		//cout << "PICK_TWO. Time spent on generating random number " << double(end_pt - begin_pt) / CLOCKS_PER_SEC << endl;
		cout << random << endl;
		vector<string> choosen = population.at(random);
		if (pair.size() == 0){
			cout << " Pushing fist one." << endl;
			pair.push_back(choosen);
		}
		else {
			int different = 0;
			vector<string> first = pair.at(0);
			if ( first != choosen ) pair.push_back(choosen);
			// for (unsigned int i = 0; i < choosen.size(); ++i){
			// 	if (choosen.at(i) != first.at(i)){
			// 		++different;
			// 		break;
			// 	}
			// }
			// if (different != 0){
			// 	pair.push_back(choosen);
			// }
		}
		++counter;
	}
	cout << "PICK_TWO. Tried to generate pair for " << counter << " times.";

	return pair;
}

int get_random_num(int mod)
{
	
	return rand() % mod ;
}

vector<vector<string>> pick_better_half(vector<vector<string>> population, 
										map<string, vector<int> > mapa, 
										unsigned int worst_possible_path_lenght)
{
	// GETTING BETTER HALF
	vector<vector<string>> better_half;
	vector<vector<string>> local_population = population;

	for (unsigned int i = 0; i < population.size()/2; ++i){
		vector<string> best_one = find_best_path(local_population, mapa, worst_possible_path_lenght);
		better_half.push_back(best_one);
		for (unsigned int j = 0; j < local_population.size(); ++j){
			if (best_one == local_population.at(j)){
				local_population.erase(
					std::remove(local_population.begin(), local_population.end(), best_one), 
					local_population.end()
				);
			}
		}
	}
	return better_half;
}

vector<string> find_best_path(vector<vector<string>> population, 
								map<string, vector<int> > mapa, 
								unsigned int worst_possible_path_lenght)
{
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

bool contains_cycles(vector<string> path)
{
	// CHECKS FOR CYCLES IN PATH
	for (unsigned int i = 0; i < path.size(); ++i){
		int check = 0;
		for (unsigned int j = 0; j < path.size(); ++j){
			if (path.at(i) == path.at(j)){
				++check;
			}
		}
		if (check > 1){
			return true;
		}
	}
	return false;
}

vector<string> get_nodes(map<string, vector<int> > mapa)
{
	// GETS ALL NODE NAMES FROM MAP AND STORES IN A STRING VECTOR
	vector<string> result;
	for (map<string, vector<int> >::iterator it = mapa.begin(); it != mapa.end(); ++it){
		result.push_back(it->first);
	}
	return result;
}

double get_distance(string s1, string s2, map<string, vector<int> > mapa)
{
	// GETS EUCLIDESIAN DISTANCE BETWEEN TWO POINS IN A PLANE
	int x1 = mapa[s1].at(0);
	int y1 = mapa[s1].at(1);
	int x2 = mapa[s2].at(0);
	int y2 = mapa[s2].at(1);
	//cout << "Calculating for " << x1 << "," << y1 << "," << x2 << "," << y2 << endl;
	return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

void print_vector(vector<string> vec)
{
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
	//cout << "\t" << get_path_length(path, mapa);
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

vector< vector<string> > create_initial_population(map<string, vector<int> > mapa, 
													unsigned int population_size)
{
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
	print_array_of_paths(population);
	for (unsigned int i = 0; i < population.size(); ++i){
		int check = 0;
		if ( contains_cycles( population.at(i))){
			++check ;
		}
		if (check > 0) {
			if (DEBUG == 1) cout << "Cycle at " << i << endl;
			if (DEBUG == 1) print_path(population.at(i));
		}
		else {
			if (DEBUG == 1) cout << "No cycke at " << i << endl;
		}
	}
	return population;
}

map<string, vector<int> > build_data_map(){

	vector<int> point;
	map<string, vector<int> > mapa;

	point.push_back(0);
	point.push_back(13);
	mapa["A"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(26);
	mapa["B"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(27);
	mapa["C"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(39);
	mapa["D"] = point;
	point.clear();

	point.push_back(2);
	point.push_back(0);
	mapa["E"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(13);
	mapa["F"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(19);
	mapa["G"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(25);
	mapa["H"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(31);
	mapa["I"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(37);
	mapa["J"] = point;
	point.clear();

	return mapa;
}
