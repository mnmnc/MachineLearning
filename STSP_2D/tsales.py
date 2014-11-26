import math
import random
import copy

mini_map = {
	"AA": {"x": 0, "y": 13},
	"AB": {"x": 0, "y": 26},
	"AC": {"x": 0, "y": 27},
	"AD": {"x": 0, "y": 39},
	"AE": {"x": 2, "y": 0},
	"AF": {"x": 5, "y": 13},
	"AG": {"x": 5, "y": 19},
	"AH": {"x": 5, "y": 25},
	"AI": {"x": 5, "y": 31},
	"AJ": {"x": 5, "y": 37}
}

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
	"""CALCULATING DISTANCE BETWEEN TWO NODES"""
	global map
	p1 = map[node_a]["x"] - map[node_b]["x"]
	p2 = map[node_a]["y"] - map[node_b]["y"]
	result = math.pow(p1, 2) + math.pow(p2, 2)
	return math.sqrt(result)

def get_path_length(nodes):
	"""CALCULATING LENGTH FOR GIVEN PATH"""
	sum = 0
	for i in range(len(nodes)-1):
		sum += get_distance(nodes[i], nodes[i+1])
	return sum

def create_initial_population(map):
	"""CREATES AN INITIAL POPULATION BY RANDOMLY REORDERING THE DATA"""

	population = []		# INITIAL POPULATION
	adam = []			# FIRST BEING

	# CREATING FIRST BEING BY PUSHING GENES
	for node in map:
		adam.append(node)

	# SHUFFLING ADAM GENES TO CREATE POPULATION
	while len(population) < len(map):
		new_being = adam[:]
		random.shuffle(new_being)
		if len(population) == 0:
			population.extend([new_being])
		else:
			# ONLY UNIQUE BEINGS ARE ACCEPTABLE
			collision_check = 0
			for being in population:
				if being == new_being:
					collision_check += 1
			if collision_check == 0:
				population.extend([new_being])
	return population

def pick_single_best_from(population):
	"""FINDS A LEADER IN POPULATION"""
	global worst_possible_path_length
	best_path_score = worst_possible_path_length
	best_path = None
	for being in population:
		being_score = get_path_length(being)
		if being_score < best_path_score:
			best_path_score = being_score
			best_path = being
	return best_path

def pick_best(population):
	"""FINDS BEST HALF OF POPULATION BASED ON SOLUTION QUALITY"""
	local_population = population[:]
	best = []
	for i in range(int(len(population)/2)):
		picked_best = pick_single_best_from(local_population)
		local_population.remove(picked_best)
		best.extend([picked_best])
	return best

def crossover(mommy, daddy):
	"""CREATES DESCENDANTS FROM PARENTS"""

	# VARIABLES
	global mutation_threshold

	# DO PARENTS LIKE EACH OTHER ENOUGH
	random.seed()
	if random.random() > 0.7:
		# IF THEY DO NOT LIKE EACH OTHER - EXIT
		return (mommy, daddy)

	# PROCEED WITH CROSSOVER
	#
	# GET RANDOM CROSSING POINTS
	crossing_point_1 = int(random.random() * len(mommy))
	crossing_point_2 = int(random.random() * len(mommy))

	smaller = 0
	bigger = 0

	# IF CROSSING POINTS ARE THE SAME - THE CROSSING IS IMPOSSIBLE
	if crossing_point_1 == crossing_point_2:
		return (mommy, daddy)

	# OTHERWISE GET CROSSING POINTS IN ORDER
	if crossing_point_1 < crossing_point_2:
		smaller = crossing_point_1
		bigger = crossing_point_2
	else:
		bigger = crossing_point_1
		smaller = crossing_point_2

	# WILL HOLD DESCENDANTS GENES
	daughter = mommy[:]
	son = daddy[:]

	# CROSS PARENTS' GENES BETWEEN CROSSING POINTS
	daughter[smaller:bigger] = daddy[smaller:bigger]
	son[smaller:bigger] = mommy[smaller:bigger]

	# REMOVE GENES FROM PRIME PARENT
	# DESCENDANT | PRIME PARENT
	# -----------+--------------
	# DAUGHTER   | MOMMY
	# SON        | DADDY
	for i in range(smaller):
		daughter[i] = ' '
		son[i] = ' '
	for i in range(bigger, len(mommy)):
		daughter[i] = ' '
		son[i] = ' '

	# COLLECT THE CROSSOVER GENES
	mommy_gene_pool = mommy[smaller:bigger]
	daddy_gene_pool = daddy[smaller:bigger]

	# CREATES RULES BASED ON GENE POOLS
	rules = []
	for i in range(len(mommy_gene_pool)):
		rules.append({mommy_gene_pool[i]:daddy_gene_pool[i]})
		rules.append({daddy_gene_pool[i]:mommy_gene_pool[i]})

	# APPLY RULES BASED ON GENE POOLS

	# FILLING DAUGHTER SUB-GENOM 1
	for i in range(smaller):
		if daughter[i] == ' ':
			for rule in rules:
				key = list(rule.keys())[0]
				if key == mommy[i]:
					daughter[i] = rule[key]

	# FILLING DAUGHTER SUB-GENOM 2
	for i in range(bigger, len(daughter)):
		if daughter[i] == ' ':
			for rule in rules:
				key = list(rule.keys())[0]
				if key == mommy[i]:
					daughter[i] = rule[key]

	# FILLING SON SUB-GENOM 1
	for i in range(smaller):
		if son[i] == ' ':
			for rule in rules:
				key = list(rule.keys())[0]
				if key == daddy[i]:
					son[i] = rule[key]

	# FILLING SON SUB-GENOM 2
	for i in range(bigger, len(son)):
		if son[i] == ' ':
			for rule in rules:
				key = list(rule.keys())[0]
				if key == daddy[i]:
					son[i] = rule[key]

	# WILL HOLD UNUSED PARENTS' GENES
	missing_in_mommy = []
	missing_in_daddy = []

	# COLLECTING UNUSED GENES FROM MOMMY
	for i in range(len(daughter)):
		if daughter[i] == ' ':
			missing_in_mommy.append(mommy[i])

	# COLLECTING UNUSED GENES FROM DADDY
	for i in range(len(son)):
		if son[i] == ' ':
			missing_in_daddy.append(daddy[i])

	# FILLING LAST EMPTY GENES IN DAUGHTER WITH DADDY GENES
	index = 0
	for i in range(len(daughter)):
		if daughter[i] == ' ':
			daughter[i] = missing_in_daddy[index]
			index+=1

	# FILLING LAST EMPTY GENES IN SON WITH MOMMY GENES
	index = 0
	for i in range(len(son)):
		if son[i] == ' ':
			son[i] = missing_in_mommy[index]
			index+=1


	# MUTATION BEGINS HERE
	#
	# MUTATING DAUGHTER
	random.seed()
	if random.random() < mutation_threshold:
		# GETTING RANDOM MUTATION POINTS
		crossing_point_1 = int(random.random() * len(mommy))
		crossing_point_2 = int(random.random() * len(mommy))

		# IF MUTATION POINTS ARE DIFFERENT
		if crossing_point_1 != crossing_point_2:
			smaller = 0
			bigger = 0

			# GET THEM IN ORDER
			if crossing_point_1 < crossing_point_2:
				smaller = crossing_point_1
				bigger = crossing_point_2
			else:
				bigger = crossing_point_1
				smaller = crossing_point_2

			# MUTATING DAUGHTER BY REVERSING RANDOM SUB-GENOM
			mutation = daughter[smaller:bigger]
			mutation.reverse()
			daughter[smaller:bigger] = mutation

	# MUTATING SON
	random.seed()
	if random.random() < mutation_threshold:
		# GETTING RANDOM MUTATION POINTS
		crossing_point_1 = int(random.random() * len(mommy))
		crossing_point_2 = int(random.random() * len(mommy))

		# IF MUTATION POINTS ARE DIFFERENT
		if crossing_point_1 != crossing_point_2:
			smaller = 0
			bigger = 0

			# GET THEM IN ORDER
			if crossing_point_1 < crossing_point_2:
				smaller = crossing_point_1
				bigger = crossing_point_2
			else:
				bigger = crossing_point_1
				smaller = crossing_point_2

			# MUTATING SON BY REVERSING RANDOM SUB-GENOM
			mutation = son[smaller:bigger]
			mutation.reverse()
			son[smaller:bigger] = mutation

	# RETURNING CROSSOVER AND MUTATION RESULTS
	result = [daughter, son]
	return result

def pick_two(population):
	"""RANDOMLY PICKS TWO BEINGS FROM GIVEN POPULATION"""
	random.seed()
	pick1 = int(random.random() * len(population))
	pick2 = 0
	while pick2 == 0 or pick2 == pick1:
		pick2 = int(random.random() * len(population))
	return (population[pick1], population[pick2])

def get_population_average(population):
	"""CALCULATES AVERAGE SOLUTION QUALITY IN GIVEN POPULATION"""
	sum = 0
	for being in population:
		sum += get_path_length(being)
	return (sum/len(population))


def solve(iterations, population):
	'''Processes TSP with given data over x iterations.'''

	# VARIABLES FOR SUMMARY PURPOSES
	best_path = []
	global worst_possible_path_length
	best_path_len = worst_possible_path_length


	iteration_index = 0
	local_population = population[:]

	# FINDING BEST SOLUTION
	for i in range(iterations):

		# NEXT POPULATION
		next_population = []

		# PICKING BEST ONES FROM CURRENT POPULATION
		current_best = pick_best(local_population)

		# UNTIL WE HAVE NEXT POPULATION
		while len(next_population) < len(population):

			# PICK POTENTIAL PARENTS
			mommy, daddy = pick_two(current_best)

			# CROSS PARENTS + POTENTIAL MUTATION
			result = crossover(mommy, daddy)
			daughter = result[0]
			son = result[1]

			# MAKE SURE SOLUTIONS GIVEN BY CHILDREN ARE ACCEPTABLE
			# AND DO NOT CROSS THE SOLUTION BOUNDARIES
			d_check = check_for_cycles(daughter)
			s_check = check_for_cycles(son)

			# IF CHILDREN ARE CORRECT AND WILL NOT CAUSE DUPLICATION IN POPULATION
			# ADD THEM TO NEXT POPULATION
			if daughter not in next_population and d_check == 0:
				next_population.append(daughter)
			if son not in next_population and s_check == 0:
				next_population.append(son)

		# IF IN NEXT POPULATION ONE SOLUTION IS SUPERIOR TO CURRENT
		# RECORD HOLDER - GIVE FIRST PLACE TO NEW BEST SOLUTION
		if get_path_length(pick_single_best_from(next_population)) < best_path_len:
			best_path_len = get_path_length(pick_single_best_from(next_population))
			best_path = pick_single_best_from(next_population)
			iteration_index = i

		# SHOW CURRENT BEST PATH
		path_length = get_path_length(pick_single_best_from(next_population))
		population_avg = get_population_average(next_population)
		print("Best path at iteration", (i+1), "has length", path_length, "[AVG]:", population_avg )

		# T + 1
		# SET NEXT POPULATION AS CURRENT ONE AND BEGIN NEXT ITERATION
		local_population = copy.deepcopy(next_population)

	# PRINT SUMMARY
	print("\nBest one:", best_path)
	print("Path len:", best_path_len)
	print("Best reached in", iteration_index ,"iteration")


def check_for_cycles(path):
	"""CHECKS IF SOLUTION DOES NOT HAVE CYCLES"""
	for node in path:
		counter = 0
		for node2 in path:
			if node == node2:
				counter+=1
		if counter > 1:
			return 1 # IF CYCLE DETECTED
	return 0 # IF NO CYCLES


def main():

	# VARIABLES
	global map, mutation_threshold, worst_possible_path_length
	maps = [mini_map, small_map, large_map]
	map = maps[1]
	mutation_threshold = 0.021
	iteration_threshold = 1000
	worst_possible_path_length = 9999999999

	# INITIATE
	population = create_initial_population(map)

	# SOLVE TSP
	solve(iteration_threshold, population)


if __name__ == "__main__":
	main()