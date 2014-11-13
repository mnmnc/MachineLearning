
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


def fill_unvisited_vertices():
	global unvisited
	unvisited = []
	for key in graph:
		print("Adding", key, "to unvisited")
		unvisited.append(key)


def fill_distance_matrix():
	global distance_matrix
	distance_matrix = {}
	for key in graph:
		if key == "A":
			print("Adding initial distance 99999 for", key)
			distance_matrix.update({key:0})
		else:
			print("Adding initial distance 99999 for", key)
			distance_matrix.update({key:99999})


def calculate_distance_to_neighbours():
	global initial_node, distance_matrix
	neighbours = graph[initial_node]
	print("Iterating over neighbours")
	for neighbour in neighbours:
		print("\tProcessing neighbour:", neighbour)
		for neighbour_name in neighbour:
			print("\t\tneighbour name:", neighbour_name)
			weight = neighbour[neighbour_name]
			print("\t\tneighbour weight:", weight)
			print("\t\t\tComparing:", str(distance_matrix[initial_node] + weight), "and", str(distance_matrix[neighbour_name])  )
			if distance_matrix[initial_node] + weight < distance_matrix[neighbour_name]:
				print("\t\t\tSMALLER!")
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
	print("Searching for closest neighbour of :", node)
	smallest_value = 99999
	closest_neighbour = None
	for neighbours in graph[node]:
		print("\tNeighbours:", neighbours)
		for neighbour_name in neighbours:
			print("\t\tNeighbour:", neighbour_name, " Nvalue:", distance_matrix[neighbour_name], " smallest", smallest_value  )
			if distance_matrix[neighbour_name] < smallest_value:
				print("\t\t\tnew smallest value", distance_matrix[neighbour_name], " node", neighbour_name )
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

	printer = pprint.PrettyPrinter(width=50)
	global initial_node, distance_matrix, unvisited, destination_node
	fill_unvisited_vertices()
	fill_distance_matrix()
	set_destination_node("Z")

	for i in range(len(graph)):
		set_initial_node(get_node_with_smallest_distance())
		print(initial_node)
		calculate_distance_to_neighbours()
		printer.pprint(distance_matrix)
		unvisited.remove(initial_node)
		printer.pprint(unvisited)

	find_reverse_path()

if __name__ == "__main__":
	main()