import math
import random
import pprint
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

medium_map = {
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
	"BZ": {"x": 25, "y": 29}
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
	#print("CROSSOVER BEGIN\n")
	#print("\tChecking for Parent cycles")
	check_for_cycles(mommie)
	check_for_cycles(daddie)
	random.seed()
	if random.random() > 0.7:
		return (mommie, daddie)

	crossing_point_1 = int(random.random() * len(mommie))
	crossing_point_2 = int(random.random() * len(mommie))
	smaller = 0
	bigger = 0

	# print("\tChecking crossing points:")
	# print("\t\tCross", crossing_point_1)
	# print("\t\tCross", crossing_point_2)

	if crossing_point_1 == crossing_point_2:
		return (mommie, daddie)

	# get smaller
	if crossing_point_1 < crossing_point_2:
		smaller = crossing_point_1
		bigger = crossing_point_2
	else:
		bigger = crossing_point_1
		smaller = crossing_point_2

	daughter = []
	son = []

	daughter = mommie[:]
	son = daddie[:]

	daughter[smaller:bigger] = daddie[smaller:bigger]
	son[smaller:bigger] = mommie[smaller:bigger]

	# print("PARENTS:")
	# print("\tMOM:", mommie)
	# print("\tDAD:", daddie)
	# print("\nCHILDREN:")
	# print("\tDAU:", daughter)
	# print("\tSON:", son)

	# print("FILLING EMPTY ONES")
	for i in range(smaller):
		daughter[i] = ' '
		son[i] = ' '

	for i in range(bigger, len(mommie)):
		daughter[i] = ' '
		son[i] = ' '


	# print("\nCHILDREN:")
	# print("\tDAU:", daughter)
	# print("\tSON:", son)

	mommie_genpool = mommie[smaller:bigger]
	daddie_genpool = daddie[smaller:bigger]

	# print("GEN POOLS")
	# print("\tM",mommie_genpool)
	# print("\tD",daddie_genpool)

	#print("CREATING RULES")
	# mommie_rules = []
	# for i in range(len(mommie_genpool)):
	# 	mommie_rules.append({mommie_genpool[i]:daddie_genpool[i]})
	#
	# daddie_rules = []
	# for i in range(len(daddie_genpool)):
	# 	daddie_rules.append({daddie_genpool[i]:mommie_genpool[i]})

	rules = []
	for i in range(len(mommie_genpool)):
		rules.append({mommie_genpool[i]:daddie_genpool[i]})
		rules.append({daddie_genpool[i]:mommie_genpool[i]})

	#print("RULES CREATED")
	#(pprint.PrettyPrinter()).pprint(rules)

	# print(" ")
	# (pprint.PrettyPrinter()).pprint(daddie_rules)

	# print("APPLYING RULES FOR DAUGHTER")
	# for i in range(len(daughter)):
	# 	print(i)
	# 	if daughter[i] == ' ':
	# 		print("Empty filed")
	# 		for rule in mommie_rules:
	# 			print("RULE",rule)
	# 			key = list(rule.keys())[0]
	# 			print("Key", key)
	# 			print("Mommie i", mommie[i])
	# 			if key == mommie[i]:
	#
	# 				daughter[i] = rule[key]
	# 				print("Setting daughter", i, "to", rule[key] )
	# 				print(daughter)
	#
	# print("APPLYING RULES FOR SON")
	# for i in range(len(son)):
	# 	if son[i] == ' ':
	# 		for rule in daddie_rules:
	# 			key = list(rule.keys())[0]
	# 			if key == daddie[i]:
	# 				son[i] = rule[key]
	# 				print("Setting son", i, "to", rule[key] )
	# 				print(son)

	# print("\nCHILDREN:")
	# print("\tDAU:", daughter)
	# print("\tSON:", son)

	for i in range(smaller):
		#print(i)
		if daughter[i] == ' ':
			#print("D Empty")
			for rule in rules:
				#print("Rule:", rule)
				key = list(rule.keys())[0]
				#print("Key", key)
				if key == mommie[i]:
					daughter[i] = rule[key]
					#print("Setting daughter", i, "to", rule[key] )
					#print(daughter)

	for i in range(bigger, len(daughter)):
		#print(i)
		if daughter[i] == ' ':
			#print("D Empty")
			for rule in rules:
				#print("Rule:", rule)
				key = list(rule.keys())[0]
				#print("Key", key)
				if key == mommie[i]:
					daughter[i] = rule[key]
					#print("Setting daughter", i, "to", rule[key] )
					#print(daughter)

	for i in range(smaller):
		#print(i)
		if son[i] == ' ':
			#print("S Empty")
			for rule in rules:
				#print("Rule:", rule)
				key = list(rule.keys())[0]
				#print("Key", key)
				if key == daddie[i]:
					son[i] = rule[key]
					#print("Setting son", i, "to", rule[key] )
					#print(son)

	for i in range(bigger, len(son)):
		#print(i)
		if son[i] == ' ':
			#print("S Empty")
			for rule in rules:
				#print("Rule:", rule)
				key = list(rule.keys())[0]
				#print("Key", key)
				if key == daddie[i]:
					son[i] = rule[key]
					#print("Setting son", i, "to", rule[key] )
					#print(son)

	missing_in_mommie = []
	missing_in_daddie = []

	for i in range(len(daughter)):
		if daughter[i] == ' ':
			missing_in_mommie.append(mommie[i])

	for i in range(len(son)):
		if son[i] == ' ':
			missing_in_daddie.append(daddie[i])

	index = 0
	for i in range(len(daughter)):
		if daughter[i] == ' ':
			daughter[i] = missing_in_daddie[index]
			index+=1

	index = 0
	for i in range(len(son)):
		if son[i] == ' ':
			son[i] = missing_in_mommie[index]
			index+=1

	# print("FINAL")
	# print("MOM:", mommie)
	# print("DAD:", daddie)

	#print("DAU:", daughter)
	#print("SON:", son)

	check_for_cycles(daughter)
	check_for_cycles(son)

	# MUTATION

	random.seed()
	if random.random() < 0.021:
		#print("\t\t\t\t MUTATION")
	#if random.random() > 0:

		crossing_point_1 = int(random.random() * len(mommie))
		crossing_point_2 = int(random.random() * len(mommie))
		if crossing_point_1 != crossing_point_2:
			smaller = 0
			bigger = 0
			# get smaller
			if crossing_point_1 < crossing_point_2:
				smaller = crossing_point_1
				bigger = crossing_point_2
			else:
				bigger = crossing_point_1
				smaller = crossing_point_2

			# print("Mutation begins at:", smaller)
			# print("Mutation ends at:", bigger)

			mutation = daughter[smaller:bigger]
			mutation.reverse()
			#print("Mutating:", daughter[smaller:bigger], "to", mutation )
			daughter[smaller:bigger] = mutation

	random.seed()
	if random.random() < 0.021:
	#if random.random() > 0:
		crossing_point_1 = int(random.random() * len(mommie))
		crossing_point_2 = int(random.random() * len(mommie))

		if crossing_point_1 != crossing_point_2:
			smaller = 0
			bigger = 0
			# get smaller
			if crossing_point_1 < crossing_point_2:
				smaller = crossing_point_1
				bigger = crossing_point_2
			else:
				bigger = crossing_point_1
				smaller = crossing_point_2

			# print("Mutation begins at:", smaller)
			# print("Mutation ends at:", bigger)

			mutation = son[smaller:bigger]
			mutation.reverse()
			#print("Mutating:", son[smaller:bigger], "to", mutation )
			son[smaller:bigger] = mutation

	# print("DAU:", daughter)
	# print("SON:", son)
	result = [daughter, son]
	return result

def pick_two(population):
	random.seed()
	pick1 = int(random.random() * len(population))
	pick2 = 0
	while pick2 == 0 or pick2 == pick1:
		pick2 = int(random.random() * len(population))

	#print("+P1", pick1, population[pick1])
	#print("+P2", pick2, population[pick2])
	return (population[pick1], population[pick2])

def get_population_average(population):
	sum = 0
	for being in population:
		sum += get_path_length(being)
	return (sum/len(population))


def solve(iterations, population):
	best_path = []
	best_path_len = 999999999
	iteration_index = 0
	local_population = population[:]
	for i in range(iterations):
		#print("\t\t\t\t\t\t\t\t\t\tITERATION", i)
		# PICKING BEST ONES
		new_population = []
		#print("Picking best of population.")
		current_best = pick_best(local_population)
		#print("Creating new population.")
		while len(new_population) < len(population):
			mommie, daddie = pick_two(current_best)
			#print("\t= MOMMIE:", mommie)
			#print("\t= DADDIE:", daddie)
			#(daughter, son) = crossover(mommie, daddie)
			result = crossover(mommie, daddie)
			daughter = result[0]
			son = result[1]
			d_check = check_for_cycles(daughter)
			s_check = check_for_cycles(son)
			if daughter not in new_population and d_check == 0:
				new_population.append(daughter)
			# else:
			# 	print("Same being already found or cycle found.")
			if son not in new_population and s_check == 0:
				new_population.append(son)
			# else:
			# 	print("Same being already found or cycle found")
		#print("New population completed.")
		#print("Best one:", pick_single_best_from(new_population))
		print("Path len:", get_path_length(pick_single_best_from(new_population)))
		#print("Population average:", get_population_average(new_population))
		if get_path_length(pick_single_best_from(new_population)) < best_path_len:
			best_path_len = get_path_length(pick_single_best_from(new_population))
			best_path = pick_single_best_from(new_population)
			iteration_index = i
		print("Population len", len(local_population))
		# for being in local_population:
		# 	print(being)
		# print(" ")
		# for being in new_population:
		# 	print(being)
		local_population = copy.deepcopy(new_population)


	print("Best one:", best_path)
	print("Path len:", best_path_len)
	print("Best reached in", iteration_index ,"interation")

def check_for_cycles(path):
	for node in path:
		counter = 0
		for node2 in path:
			if node == node2:
				counter+=1
		if counter > 1:
			#print("Cycle found for node", node)
			return 1
	return 0


def main():
	printer = pprint.PrettyPrinter(indent=4)
	population = create_initial_population(small_map)

	solve(1000, population)

	# for being in population:
	# 	print(being)
	#
	#
	# print("Picking best of population.")
	#
	# current_best = pick_best(population)
	#
	# new_population = []
	#
	# print("Creating new population.")
	# while len(new_population) < len(population):
	# 	mommie, daddie = pick_two(current_best)
	# 	daughter, son = crossover(mommie, daddie)
	# 	new_population.append(daughter)
	# 	new_population.append(son)
	#
	# print("New population completed.")
	# for being in new_population:
	# 	print(being)
	#
	#
	# print("Best one:", pick_single_best_from(population))
	# print("Path len:", get_path_length(pick_single_best_from(population)))
	# print("Population average:", get_population_average(population))
	# print("NBest one:", pick_single_best_from(new_population))
	# print("NPath len:", get_path_length(pick_single_best_from(new_population)))
	# print("Population average:", get_population_average(new_population))
	#
	#
	#
	# new_population2 = []
	# current_best = pick_best(new_population)
	#
	#
	# print("Creating new population.")
	# while len(new_population2) < len(new_population):
	# 	mommie, daddie = pick_two(current_best)
	# 	daughter, son = crossover(mommie, daddie)
	# 	new_population2.append(daughter)
	# 	new_population2.append(son)
	#
	#
	# print("New population completed.")
	# for being in new_population2:
	# 	print(being)
	#
	# print("Best one:", pick_single_best_from(population))
	# print("Path len:", get_path_length(pick_single_best_from(population)))
	# print("Population average:", get_population_average(population))
	# print("NBest one:", pick_single_best_from(new_population))
	# print("NPath len:", get_path_length(pick_single_best_from(new_population)))
	# print("Population average:", get_population_average(new_population))
	# print("N2Best one:", pick_single_best_from(new_population2))
	# print("N2Path len:", get_path_length(pick_single_best_from(new_population2)))
	# print("Population average:", get_population_average(new_population2))

	#mom = ['AU', 'AA', 'AF', 'AE', 'AQ', 'AC', 'AX', 'AO', 'AI', 'AK', 'AN', 'AB', 'AW', 'AL', 'AP', 'AG', 'AZ', 'AT', 'AH', 'AY', 'AJ', 'AS', 'AV', 'AM', 'AR', 'AD']
	#dad = ['AI', 'AL', 'AC', 'AY', 'AZ', 'AQ', 'AH', 'AG', 'AR', 'AP', 'AW', 'AM', 'AV', 'AS', 'AE', 'AT', 'AX', 'AU', 'AN', 'AA', 'AK', 'AO', 'AB', 'AF', 'AD', 'AJ']

	#crossover(mom, dad)

	# CROSSOVER





if __name__ == "__main__":
	main()