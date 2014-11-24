import math
import random
import pprint
import copy

small_map = {
	"AA": {"x": 0, "y": 13},
	"AB": {"x": 0, "y": 26},
	"AC": {"x": 0, "y": 27},
	"AD": {"x": 0, "y": 39},
	"AE": {"x": 2, "y": 0},
	"AF": {"x": 5, "y": 13},
	"AG": {"x": 5, "y": 19},
	"AH": {"x": 5, "y": 25},
	"AI": {"x": 5, "y": 31},
	"AJ": {"x": 5, "y": 37},
	"AK": {"x": 5, "y": 43},
	"AL": {"x": 5, "y": 8},
	"AM": {"x": 8, "y": 0},
	"AN": {"x": 9, "y": 10},
	"AO": {"x": 10, "y": 10},
	"AP": {"x": 11, "y": 10},
	"AQ": {"x": 12, "y": 10},
	"AR": {"x": 12, "y": 5},
	"AS": {"x": 15, "y": 13},
	"AT": {"x": 15, "y": 19},
	"AU": {"x": 15, "y": 25},
	"AV": {"x": 15, "y": 31},
	"AW": {"x": 15, "y": 37},
	"AX": {"x": 15, "y": 43},
	"AY": {"x": 15, "y": 8},
	"AZ": {"x": 18, "y": 11}
}

large_map = {
	"AA": {"x": 0, "y": 13},
	"AB": {"x": 0, "y": 26},
	"AC": {"x": 0, "y": 27},
	"AD": {"x": 0, "y": 39},
	"AE": {"x": 2, "y": 0},
	"AF": {"x": 5, "y": 13},
	"AG": {"x": 5, "y": 19},
	"AH": {"x": 5, "y": 25},
	"AI": {"x": 5, "y": 31},
	"AJ": {"x": 5, "y": 37},
	"AK": {"x": 5, "y": 43},
	"AL": {"x": 5, "y": 8},
	"AM": {"x": 8, "y": 0},
	"AN": {"x": 9, "y": 10},
	"AO": {"x": 10, "y": 10},
	"AP": {"x": 11, "y": 10},
	"AQ": {"x": 12, "y": 10},
	"AR": {"x": 12, "y": 5},
	"AS": {"x": 15, "y": 13},
	"AT": {"x": 15, "y": 19},
	"AU": {"x": 15, "y": 25},
	"AV": {"x": 15, "y": 31},
	"AW": {"x": 15, "y": 37},
	"AX": {"x": 15, "y": 43},
	"AY": {"x": 15, "y": 8},
	"AZ": {"x": 18, "y": 11},
	"BA": {"x": 18, "y": 13},
	"BB": {"x": 18, "y": 15},
	"BC": {"x": 18, "y": 17},
	"BD": {"x": 18, "y": 19},
	"BE": {"x": 18, "y": 21},
	"BF": {"x": 18, "y": 23},
	"BG": {"x": 18, "y": 25},
	"BH": {"x": 18, "y": 27},
	"BI": {"x": 18, "y": 29},
	"BJ": {"x": 18, "y": 31},
	"BK": {"x": 18, "y": 33},
	"BL": {"x": 18, "y": 35},
	"BM": {"x": 18, "y": 37},
	"BN": {"x": 18, "y": 39},
	"BO": {"x": 18, "y": 41},
	"BP": {"x": 18, "y": 42},
	"BQ": {"x": 18, "y": 44},
	"BR": {"x": 18, "y": 45},
	"BS": {"x": 25, "y": 11},
	"BT": {"x": 25, "y": 15},
	"BU": {"x": 25, "y": 22},
	"BV": {"x": 25, "y": 23},
	"BW": {"x": 25, "y": 24},
	"BX": {"x": 25, "y": 26},
	"BY": {"x": 25, "y": 28},
	"BZ": {"x": 25, "y": 29},
	"CA": {"x": 25, "y": 9},
	"CB": {"x": 28, "y": 16},
	"CC": {"x": 28, "y": 20},
	"CD": {"x": 28, "y": 28},
	"CE": {"x": 28, "y": 30},
	"CF": {"x": 28, "y": 34},
	"CG": {"x": 28, "y": 40},
	"CH": {"x": 28, "y": 43},
	"CI": {"x": 28, "y": 47},
	"CJ": {"x": 32, "y": 26},
	"CK": {"x": 32, "y": 31},
	"CL": {"x": 33, "y": 15},
	"CM": {"x": 33, "y": 26},
	"CN": {"x": 33, "y": 29},
	"CO": {"x": 33, "y": 31},
	"CP": {"x": 34, "y": 15},
	"CQ": {"x": 34, "y": 26},
	"CR": {"x": 34, "y": 29},
	"CS": {"x": 34, "y": 31},
	"CT": {"x": 34, "y": 38},
	"CU": {"x": 34, "y": 41},
	"CV": {"x": 34, "y": 5},
	"CW": {"x": 35, "y": 17},
	"CX": {"x": 35, "y": 31},
	"CY": {"x": 38, "y": 16},
	"CZ": {"x": 38, "y": 20},
	"DA": {"x": 38, "y": 30},
	"DB": {"x": 38, "y": 34},
	"DC": {"x": 40, "y": 22},
	"DD": {"x": 41, "y": 23},
	"DE": {"x": 41, "y": 32},
	"DF": {"x": 41, "y": 34},
	"DG": {"x": 41, "y": 35},
	"DH": {"x": 41, "y": 36},
	"DI": {"x": 48, "y": 22},
	"DJ": {"x": 48, "y": 27},
	"DK": {"x": 48, "y": 6},
	"DL": {"x": 51, "y": 45},
	"DM": {"x": 51, "y": 47},
	"DN": {"x": 56, "y": 25},
	"DO": {"x": 57, "y": 12},
	"DP": {"x": 57, "y": 25},
	"DQ": {"x": 57, "y": 44},
	"DR": {"x": 61, "y": 45},
	"DS": {"x": 61, "y": 47},
	"DT": {"x": 63, "y": 6},
	"DU": {"x": 64, "y": 22},
	"DV": {"x": 71, "y": 11},
	"DW": {"x": 71, "y": 13},
	"DX": {"x": 71, "y": 16},
	"DY": {"x": 71, "y": 45},
	"DZ": {"x": 71, "y": 47},
	"EA": {"x": 74, "y": 12},
	"EB": {"x": 74, "y": 16},
	"EC": {"x": 74, "y": 20},
	"EF": {"x": 74, "y": 24},
	"EG": {"x": 74, "y": 29},
	"EH": {"x": 74, "y": 35},
	"EI": {"x": 74, "y": 39},
	"EJ": {"x": 74, "y": 6},
	"EK": {"x": 77, "y": 21},
	"EL": {"x": 78, "y": 10},
	"EM": {"x": 78, "y": 32},
	"EN": {"x": 78, "y": 35},
	"EO": {"x": 78, "y": 39},
	"EP": {"x": 79, "y": 10},
	"EQ": {"x": 79, "y": 33},
	"ER": {"x": 79, "y": 37},
	"ES": {"x": 80, "y": 10},
	"ET": {"x": 80, "y": 41},
	"EU": {"x": 80, "y": 5},
	"EV": {"x": 81, "y": 17},
	"EW": {"x": 84, "y": 20},
	"EX": {"x": 84, "y": 24},
	"EY": {"x": 84, "y": 29},
	"EZ": {"x": 84, "y": 34},
	"FA": {"x": 84, "y": 38},
	"FB": {"x": 84, "y": 6},
	"FC": {"x": 107, "y": 27}
}


def get_distance(node_a, node_b):
	p1 = small_map[node_a]["x"] - small_map[node_b]["x"]
	p2 = small_map[node_a]["y"] - small_map[node_b]["y"]
	result = math.pow(p1, 2) + math.pow(p2, 2)
	return math.sqrt(result)

def get_path_length(nodes):
	sum = 0
	for i in range(len(nodes)-1):
		sum += get_distance(nodes[i], nodes[i+1])
	return sum

def create_initial_population(map):
	population = []
	adam = []
	for node in map:
		adam.append(node)
	while len(population) < len(map):
		new_being = adam[:]
		random.shuffle(new_being)
		if len(population) == 0:
			population.extend([new_being])
		else:
			collision_check = 0
			for being in population:
				if being == new_being:
					collision_check += 1
			if collision_check == 0:
				population.extend([new_being])
	return population

def pick_single_best_from(population):
	best_path_score = 999999
	best_path = None
	for being in population:
		being_score = get_path_length(being)
		if being_score < best_path_score:
			best_path_score = being_score
			best_path = being
	return best_path

def pick_best(population):
	local_population = population[:]
	best = []
	for i in range(int(len(population)/2)):
		picked_best = pick_single_best_from(local_population)
		local_population.remove(picked_best)
		best.extend([picked_best])
	return best

def crossover(mommie, daddie):
	random.seed()
	crossing_point_1 = int(random.random() * len(mommie))
	crossing_point_2 = int(random.random() * len(mommie))
	smaller = 0
	bigger = 0

	if crossing_point_1 == crossing_point_2:
		return (mommie, daddie)
	else:
		# get smaller
		if crossing_point_1 < crossing_point_2:
			smaller = crossing_point_1
			bigger = crossing_point_2
		else:
			bigger = crossing_point_1
			smaller = crossing_point_2

	


def main():
	printer = pprint.PrettyPrinter(indent=4)
	population = create_initial_population(small_map)

	# PICK BEST
	print("Best:")
	current_best = pick_best(population)

	# CROSSOVER
	new_population = copy.deepcopy(current_best)




if __name__ == "__main__":
	main()