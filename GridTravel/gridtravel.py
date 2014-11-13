
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


def fill_unvisited_verticies():
	global unvisited
	for key in graph:
		print("Adding", key, "to unvisited")
		unvisited.append(key)


def fill_distance_matrix():
	global distance_matrix
	for key in graph:
		print("Adding initial distance 99999 for", key)
		distance_matrix.update({key:99999})


def calculate_distance_to_neighbours():
	global initial_node, distance_matrix
	neighbours = graph[initial_node]
	for neighbour in neighbours:
		weight = neighbours[neighbour]
		if distance_matrix[initial_node] + weight < distance_matrix[neighbour]:
			distance_matrix[neighbour] = distance_matrix[initial_node] + weight

def get_node_with_smalles_distance():
	global distance_matrix, unvisited
	smallest_distance_node = None
	for node in unvisited:
		if smallest_distance_node == None:
			smallest_distance_node = node
		else:
			if distance_matrix[smallest_distance_node] > distance_matrix[node]:
				smallest_distance_node = node

def process_nodes():
	pass