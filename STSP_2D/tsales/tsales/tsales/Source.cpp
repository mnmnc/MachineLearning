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
	void print_path(vector<string> path);
	void print_path_and_values(vector<string> path, map<string, vector<int> > mapa);
	void print_array_of_paths(vector<vector<string>> path_array);
	void print_array_of_paths_and_values(vector<vector<string>> path_array, map<string, vector<int> > mapa);

// DISTANCE CALCULATION
	double get_distance(string s1, string s2, map<string, vector<int> > mapa);
	double get_path_length(vector<string> nodes, map<string, vector<int> > mapa);
	double get_path_length(vector<string> nodes, map<string, vector<int> > mapa);

// COMPARE FUNCTIONS
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

	// SEEDING
	srand(time(NULL));
	
	// BUILDING DATA MAP
	map<string, vector<int> > mapa = build_data_map();
	population_size = mapa.size();

	// CREATING INITIAL POPULATION
	vector<vector<string>> population_1 = create_initial_population(mapa, population_size);

	// SOLVING
	clock_t begin_pt = clock();
	solve(population_1, mapa, iteration_threshold);
	//clock_t end_pt = clock();
	std::cout << "Time spent solving " << double(clock() - begin_pt) / CLOCKS_PER_SEC << endl;

	system("PAUSE");
	return 0;
	
}

void solve(vector<vector<string>> population_1, map<string, vector<int> > mapa, int iterations){

	double best_path_length = UINT_MAX;
	vector<string> best_path;
	unsigned int best_path_reached_in_iteration = 0;
	unsigned int iteration_counter = 0;
	unsigned int total_iterations = iterations;
	vector<vector<string>> local_population = population_1;

	// GENERATE GIVEN NUMBER OF GENERATIONS
	while ( iterations > 0 ){
		vector<vector<string>> next_population;
		vector<vector<string>> better_half = pick_better_half(local_population, mapa, UINT_MAX);

		// FILL WHOLE POPULATION
		//while (next_population.size() < (population_1.size() /1.5)){
		while (next_population.size() < population_1.size()){

			// PICKING PARENTS
			vector<vector<string>> parents = pick_two(better_half);

			// CROSSING CHILDREN
			vector<vector<string>> children = crossover(parents, mapa);

			// MUTATING CHILDREN
			children = mutation(children, mapa);

			// VERIFYING CHILDREN VALIDITY
			bool cycles_in_daughter = contains_cycles(children.at(0));
			bool cycles_in_son = contains_cycles(children.at(1));

			// IF NOT TWINS
			if (children.at(0) != children.at(1)){
				if ( next_population.size() < 1 ){
					// IF POPULATION IS FRESH - EXTEND IT WITHOUT CHECKING
					if (!cycles_in_daughter) next_population.push_back(children.at(0));
					if (!cycles_in_son) next_population.push_back(children.at(1));
				}
				else {
					// CHECK FOR POTENTIAL GENE DUPLICATION
					int daughter_check = 0;
					int son_check = 0;
					for (unsigned int i = 0;  i < next_population.size(); ++i){
						if (children.at(0) == next_population.at(i)) ++daughter_check;
						if (children.at(1) == next_population.at(i)) ++son_check;
					}
					// ADD THOSE THAT WILL BE UNIQUE IN POPULATION
					if (daughter_check < 1 && !cycles_in_daughter) next_population.push_back(children.at(0));
					if (son_check < 1 && !cycles_in_son) next_population.push_back(children.at(1));
				}
			}
			// IF TWINS - CHOOSE ONE
			else {
				// CHECK FOR POTENTIAL GENE DUPLICATION
				int daughter_check = 0;
				for (unsigned int i = 0; i < next_population.size(); ++i){
					if (children.at(0) == next_population.at(i)){
						++daughter_check;
					}
				}
				if (daughter_check < 1 && !cycles_in_daughter) next_population.push_back(children.at(0));
			}
		}

		// PICK BEST PATH AND GET LENGTH
		vector<string> local_best_path = find_best_path(next_population, mapa, UINT_MAX);
		double local_best_path_length = get_path_length(local_best_path, mapa);

		// INFORM ABOUT CURRENT ITERATION
		cout << "[INFO] Iteration " << iteration_counter+1 << ". Best path length: " << local_best_path_length << endl;

		// CHECK IF CURRENT ONE IS BEST
		if (local_best_path_length < best_path_length) {
			best_path_length = local_best_path_length;
			best_path = local_best_path;
			best_path_reached_in_iteration = total_iterations - iterations;
		}
		// T = T+1
		local_population = next_population;
		++iteration_counter;
		--iterations;
	}
	cout << "[FINAL] Best path length: " << best_path_length << " reached in " << best_path_reached_in_iteration << " iteration." << endl;

}

vector<vector<string>> mutation(vector<vector<string>> children, map<string, vector<int> > mapa){

	// MUTATION HAPPENS FOR 0.02 PERCENTILE
	if (get_random_num(1000) > 21){
		return children;
	} 

	// VARIABLES
	vector<vector<string>> mutated_children;
	vector<string> daughter = children.at(0);
	vector<string> son = children.at(1);

	// CHOOSE MUTATION POINTS
	int mutation_point_1 = get_random_num( (children.at(0)).size() );
	int mutation_point_2 = get_random_num( (children.at(0)).size() );
	while (mutation_point_1 == mutation_point_2){
		mutation_point_2 = get_random_num( (children.at(0)).size() );
	}

	// GET CROSSING POINTS IN ORDER
	unsigned int smaller = (mutation_point_1 < mutation_point_2)?(mutation_point_1):(mutation_point_2);
	unsigned int bigger = (mutation_point_1 < mutation_point_2)?(mutation_point_2):(mutation_point_1);

	// COLLECTING SUBPATH FOR MUTATION
	vector<string> daughter_mutation;
	vector<string> son_mutation;
	for (unsigned int i = smaller; i < bigger; ++i){
		daughter_mutation.push_back(daughter.at(i));
		son_mutation.push_back(son.at(i));
	}

	// REORDERING SUBGENOMS
	reverse(daughter_mutation.begin(), daughter_mutation.end());
	reverse(son_mutation.begin(), son_mutation.end());

	// MUTATING
	unsigned int index = 0;
	for (unsigned int i = smaller; i < bigger; ++i){
		daughter[i] = daughter_mutation.at(index);
		son[i] = son_mutation.at(index);
		++index;
	}

	// FILLING THE RESULT
	mutated_children.push_back(daughter);
	mutated_children.push_back(son);

	return mutated_children;
}


vector<vector<string>> crossover(vector<vector<string>> parents, map<string, vector<int> > mapa){
	// CREATES DESCENDANTS
	vector<vector<string>> children;

	// CHECK WHETHER PARENTS LIKE EACH OTHER ENOUGH
	if ( get_random_num(100) > 70 ) return parents;

	// CHOOSE CROSSING POINTS
	int crossing_point_1 = get_random_num( (parents.at(0)).size() );
	int crossing_point_2 = get_random_num( (parents.at(0)).size() );
	while ( crossing_point_1 == crossing_point_2){
		crossing_point_2 = get_random_num( (parents.at(0)).size() );
	}

	// GET CROSSING POINTS IN ORDER
	unsigned int smaller = (crossing_point_1 < crossing_point_2)?(crossing_point_1):(crossing_point_2);
	unsigned int bigger = (crossing_point_1 < crossing_point_2)?(crossing_point_2):(crossing_point_1);

	vector<string> daughter;
	vector<string> son;

	// FILLING CHILDREN WITH EMPTY GENES
	for (unsigned int i = 0; i < (parents.at(0)).size(); ++i ){
		daughter.push_back(" ");
		son.push_back(" ");
	}

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

	// COLLECTING UNUSED GENES FROM MOMMY
	vector<string> unused_mommy_genes;
	vector<string> unused_daddy_genes;
	for (unsigned int i = 0; i < daughter.size(); ++i){
		if (daughter.at(i) == " ") unused_mommy_genes.push_back( (parents.at(0)).at(i) ); 
	}
	for (unsigned int i = 0; i < son.size(); ++i){
		if (son.at(i) == " ") unused_daddy_genes.push_back( (parents.at(1)).at(i) ); 
	}

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

	// FILLING THE RESULT
	children.push_back(daughter);
	children.push_back(son);
	return children;
}

vector<vector<string>> pick_two(vector<vector<string>> population)
{
	// PICKS RANDOM TWO FROM POPULATION
	vector<vector<string>> pair;
	
	while (pair.size() != 2){

		// CHOOSING RANDOM FROM POPULATION
		unsigned int random = get_random_num( population.size() );
		vector<string> choosen = population.at(random);

		// IF THIS IS FIRST ONE - ASSIGN TO PAIR
		if (pair.size() == 0){
			pair.push_back(choosen);
		}
		// ELSE ASSIGN TO PAIR ONLY IF CHOSEN ONE IS DIFFERENT
		else {
			if (pair.at(0) != choosen) pair.push_back(choosen);
		}
	}
	return pair;
}

int get_random_num(int mod)
{
	return rand() % mod;
}

vector<vector<string>> pick_better_half(vector<vector<string>> population, map<string, vector<int> > mapa, unsigned int worst_possible_path_lenght)
{
	// GETTING BETTER HALF OF POPULATION FOR POTENCIAL CROSSOVER
	vector<vector<string>> better_half;
	vector<vector<string>> local_population = population;

	// PICKING BEST OF THE BEST ONE BY ONE
	for (unsigned int i = 0; i < population.size()/2; ++i){

		// PICK SINGLE BEST
		vector<string> best_one = find_best_path(local_population, mapa, worst_possible_path_lenght);
		better_half.push_back(best_one);

		// REMOVING CURRENT PICK FROM POPULATION
		for (unsigned int j = 0; j < local_population.size(); ++j){
			if (best_one == local_population.at(j)){
				// REMOVAL
				local_population.erase(
					std::remove(local_population.begin(), local_population.end(), best_one), 
					local_population.end()
				);
			}
		}
	}
	return better_half;
}

vector<string> find_best_path(vector<vector<string>> population, map<string, vector<int> > mapa, unsigned int worst_possible_path_lenght)
{
	// FINDS BEST SOLUTION IN POPULATION
	vector <string> best_path;
	double best_path_length = worst_possible_path_lenght;

	// ITERATING OVER ALL POPULATION
	for (unsigned int i = 0; i < population.size(); ++i){
		double length = get_path_length(population.at(i), mapa);
		if (length < best_path_length){
			// BEST ONE FOUND
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
				// CYCLE FOUND
				++check;
				if (check > 1) return true;
			}
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
	return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

void print_path(vector<string> path){
	// PRINTS PATH
	for (unsigned int i = 0; i < path.size(); ++i){
		cout << path.at(i) << " ";
	}
	cout << endl;
}

void print_path_and_values(vector<string> path, map<string, vector<int> > mapa){
	// PRINTS PATH
	for (unsigned int i = 0; i < path.size(); ++i){
		cout << path.at(i) << " ";
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

vector< vector<string> > create_initial_population(map<string, vector<int> > mapa, unsigned int population_size){
	// CREATES INITIAL POPULATION
	vector<vector<string>> population;
	vector<string> adam = get_nodes(mapa);

	// FILL WHOLE POPULATION
	while (population.size() < population_size){

		// GENE REORDERING OF FIRST BEING
		vector<string> being = shuffle(adam);
		if (population.size() < 1){
			population.push_back(being);
		}
		else {
			// ADD ONLY THE ONES THAT WILL CONTAIN UNIQUE 
			// ORDERS OF GENES IN POPULATION
			unsigned int check = 0;
			for (unsigned int i = 0; i < population.size(); ++i){
				if (being == population.at(i)){
					++check;
				}
			}
			if (check == 0){
				population.push_back(being);
			}
		}
	}
	// CHECK FOR CYCLES IN POPULATION
	for (unsigned int i = 0; i < population.size(); ++i){
		if ( contains_cycles( population.at(i))){
			cout << "[ERR] F2: Cycle detected at " << i << endl;
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
