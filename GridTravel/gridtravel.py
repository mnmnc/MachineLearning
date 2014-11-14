
# K---P---T---X---Z
# |   |   |   |   |
# G---L---Q---U---Y
# |   |   |   |   |
# D---H---M---R---W
# |   |   |   |   |
# B---E---I---N---S
# |   |   |   |   |
# A---C---F---J---O

# K-3-P-3-T-3-X-2-Z
# |25 |10 |4  |3  |2
# G-1-L-2-Q-2-U-2-Y
# |20 |8  |3  |2  |3
# D-2-H-3-M-2-R-1-W
# |10 |4  |2  |3  |2
# B-3-E-2-I-2-N-2-S
# |6  |4  |3  |3  |2
# A-4-C-1-F-2-J-3-O

import pprint
from colorama import init, Fore, Back, Style


graph = {
	'A' : [ {'B':6},	{'C':4} ],
	'K' : [ {'G':25},	{'P':3} ],
	'Z' : [ {'X':2},	{'Y':2} ],
	'O' : [ {'J':3},	{'S':2} ],
	'B' : [ {'A':6},	{'D':10},	{'E':3} ],
	'D' : [ {'B':10},	{'H':2},	{'G':20} ],
	'G' : [ {'K':25},	{'D':20},	{'L':1} ],
	'P' : [ {'K':3},	{'L':10},	{'T':3} ],
	'T' : [ {'P':3},	{'Q':4},	{'X':3} ],
	'X' : [ {'T':3},	{'U':3},	{'Z':2} ],
	'Y' : [ {'Z':2},	{'U':2},	{'W':3} ],
	'W' : [ {'Y':3},	{'R':1},	{'S':2} ],
	'S' : [ {'W':2},	{'N':2},	{'O':2} ],
	'J' : [ {'O':3},	{'N':3},	{'F':2} ],
	'F' : [ {'J':2},	{'I':3},	{'C':1} ],
	'C' : [ {'F':1},	{'E':4},	{'A':4} ],
	'E' : [ {'B':3},	{'C':4},	{'H':4},	{'I':2} ],
	'H' : [ {'D':2},	{'E':4},	{'L':8},	{'M':3} ],
	'L' : [ {'H':8},	{'G':1},	{'P':10},	{'Q':2} ],
	'Q' : [ {'L':2},	{'T':4},	{'U':2},	{'M':3} ],
	'U' : [ {'Q':2},	{'X':3},	{'R':2},	{'Y':2} ],
	'R' : [ {'U':2},	{'W':1},	{'N':3},	{'M':2} ],
	'N' : [ {'R':3},	{'S':2},	{'J':3},	{'I':2} ],
	'I' : [ {'M':2},	{'N':2},	{'F':3},	{'E':2} ],
	'M' : [ {'I':2},	{'H':3},	{'Q':3},	{'R':2} ]
}

def set_initial_node(node):
	global initial_node
	initial_node = node


def set_destination_node(node):
	global destination_node
	destination_node = node


def show_graph():
	global distance_matrix
	_A = "A"
	_B = "B"
	_C = "C"
	_D = "D"
	_E = "E"
	_F = "F"
	_G = "G"
	_H = "H"
	_I = "I"
	_J = "J"
	_K = "K"
	_L = "L"
	_M = "M"
	_N = "N"
	_O = "O"
	_P = "P"
	_Q = "Q"
	_R = "R"
	_S = "S"
	_T = "T"
	_U = "U"
	_W = "W"
	_X = "X"
	_Y = "Y"
	_Z = "Z"
	if distance_matrix["A"] < 99999: _A = Fore.RED + str(distance_matrix["A"]) + Fore.RESET
	if distance_matrix["B"] < 99999: _B = Fore.RED + str(distance_matrix["B"]) + Fore.RESET
	if distance_matrix["C"] < 99999: _C = Fore.RED + str(distance_matrix["C"]) + Fore.RESET
	if distance_matrix["D"] < 99999: _D = Fore.RED + str(distance_matrix["D"]) + Fore.RESET
	if distance_matrix["E"] < 99999: _E = Fore.RED + str(distance_matrix["E"]) + Fore.RESET
	if distance_matrix["F"] < 99999: _F = Fore.RED + str(distance_matrix["F"]) + Fore.RESET
	if distance_matrix["G"] < 99999: _G = Fore.RED + str(distance_matrix["G"]) + Fore.RESET
	if distance_matrix["H"] < 99999: _H = Fore.RED + str(distance_matrix["H"]) + Fore.RESET
	if distance_matrix["I"] < 99999: _I = Fore.RED + str(distance_matrix["I"]) + Fore.RESET
	if distance_matrix["J"] < 99999: _J = Fore.RED + str(distance_matrix["J"]) + Fore.RESET
	if distance_matrix["K"] < 99999: _K = Fore.RED + str(distance_matrix["K"]) + Fore.RESET
	if distance_matrix["L"] < 99999: _L = Fore.RED + str(distance_matrix["L"]) + Fore.RESET
	if distance_matrix["M"] < 99999: _M = Fore.RED + str(distance_matrix["M"]) + Fore.RESET
	if distance_matrix["N"] < 99999: _N = Fore.RED + str(distance_matrix["N"]) + Fore.RESET
	if distance_matrix["O"] < 99999: _O = Fore.RED + str(distance_matrix["O"]) + Fore.RESET
	if distance_matrix["P"] < 99999: _P = Fore.RED + str(distance_matrix["P"]) + Fore.RESET
	if distance_matrix["Q"] < 99999: _Q = Fore.RED + str(distance_matrix["Q"]) + Fore.RESET
	if distance_matrix["R"] < 99999: _R = Fore.RED + str(distance_matrix["R"]) + Fore.RESET
	if distance_matrix["S"] < 99999: _S = Fore.RED + str(distance_matrix["S"]) + Fore.RESET
	if distance_matrix["T"] < 99999: _T = Fore.RED + str(distance_matrix["T"]) + Fore.RESET
	if distance_matrix["U"] < 99999: _U = Fore.RED + str(distance_matrix["U"]) + Fore.RESET
	if distance_matrix["W"] < 99999: _W = Fore.RED + str(distance_matrix["W"]) + Fore.RESET
	if distance_matrix["X"] < 99999: _X = Fore.RED + str(distance_matrix["X"]) + Fore.RESET
	if distance_matrix["Y"] < 99999: _Y = Fore.RED + str(distance_matrix["Y"]) + Fore.RESET
	if distance_matrix["Z"] < 99999: _Z = Fore.RED + str(distance_matrix["Z"]) + Fore.RESET

	# print("K---P---T---X---Z")
	# print("|   |   |   |   |")
	# print("G---L---Q---U---Y")
	# print("|   |   |   |   |")
	# print("D---H---M---R---W")
	# print("|   |   |   |   |")
	# print("B---E---I---N---S")
	# print("|   |   |   |   |")
	# print("A---C---F---J---O")

	print( str(_K) + "\t" + str(_P) + "\t" + str(_T) + "\t" + str(_X) + "\t" + str(_Z))
	print("|\t|\t|\t|\t|")
	print( str(_G) + "\t" + str(_L) + "\t" + str(_Q) + "\t" + str(_U) + "\t" + str(_Y))
	print("|\t|\t|\t|\t|")
	print( str(_D) + "\t" + str(_H) + "\t" + str(_M) + "\t" + str(_R) + "\t" + str(_W))
	print("|\t|\t|\t|\t|")
	print( str(_B) + "\t" + str(_E) + "\t" + str(_I) + "\t" + str(_N) + "\t" + str(_S))
	print("|\t|\t|\t|\t|")
	print( str(_A) + "\t" + str(_C) + "\t" + str(_F) + "\t" + str(_J) + "\t" + str(_O))




def fill_unvisited_vertices():
	global unvisited
	unvisited = []
	for key in graph:
		unvisited.append(key)


def fill_distance_matrix():
	global distance_matrix
	distance_matrix = {}
	for key in graph:
		if key == "A":
			distance_matrix.update({key:0})
		else:
			distance_matrix.update({key:99999})


def calculate_distance_to_neighbours():
	global initial_node, distance_matrix
	neighbours = graph[initial_node]
	for neighbour in neighbours:
		for neighbour_name in neighbour:
			weight = neighbour[neighbour_name]
			if distance_matrix[initial_node] + weight < distance_matrix[neighbour_name]:
				distance_matrix[neighbour_name] = distance_matrix[initial_node] + weight


def get_node_with_smallest_distance():
	global distance_matrix, unvisited
	smallest_value = 99999
	smallest_distance_node = None
	for node in unvisited:
		if distance_matrix[node] < smallest_value:
			smallest_value = distance_matrix[node]
			smallest_distance_node = node
	if smallest_value == 99999:
		return "A"
	else:
		return smallest_distance_node

def get_closer_neighbour(node):
	smallest_value = 99999
	closest_neighbour = None
	for neighbours in graph[node]:
		for neighbour_name in neighbours:
			if distance_matrix[neighbour_name] < smallest_value:
				smallest_value = distance_matrix[neighbour_name]
				closest_neighbour = neighbour_name
	return closest_neighbour

def find_reverse_path():
	global destination_node, initial_node
	print("Shortest path from Z to A:")
	current_node = destination_node
	for node in graph:
		print(current_node)
		if current_node == "A":
			break
		current_node = get_closer_neighbour(current_node)




def process_nodes():
	pass

def main():
	init()
	printer = pprint.PrettyPrinter(width=50)
	global initial_node, distance_matrix, unvisited, destination_node
	fill_unvisited_vertices()
	fill_distance_matrix()
	set_destination_node("Z")

	for i in range(len(graph)):
		set_initial_node(get_node_with_smallest_distance())
		print("\nCalculating from: ",initial_node)
		calculate_distance_to_neighbours()
		#printer.pprint(distance_matrix)
		show_graph()
		unvisited.remove(initial_node)
		#printer.pprint(unvisited)

	find_reverse_path()

if __name__ == "__main__":
	main()