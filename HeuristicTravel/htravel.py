
dist = {
	'Bucharest': 		0,
	'Giurgiu': 			77,
	'Urziceni': 		80,
	'Pitesti': 			98,
	'Craiova': 			160,
	'Fagaras': 			178,
	'Rimnicu Vilcea': 	193,
	'Mehadia': 			241,
	'Dobreta': 			242,
	'Lugoj': 			244,
	'Sibiu': 			253,
	'Timisoara': 		329,
	'Arad': 			366,
	'Zerind': 			374,
	'Oradea': 			380
}

neighbours = {
	'Giurgiu': 			['Bucharest'	],
	'Fagaras':			['Bucharest', 	'Sibiu'		],
	'Lugoj': 			['Timisoara', 	'Mehadia'	],
	'Mehadia': 			['Dobreta', 	'Lugoj'		],
	'Oradea': 			['Zerind', 		'Sibiu'		],
	'Timisoara': 		['Arad', 		'Lugoj'		],
	'Zerind':			['Arad', 		'Oradea'	],
	'Arad': 			['Zerind', 		'Timisoara', 		'Sibiu'		],
	'Craiova': 			['Dobreta', 	'Rimnicu Vilcea', 	'Pitesti'	],
	'Pitesti': 			['Bucharest', 	'Rimnicu Vilcea', 	'Craiova'	],
	'Dobreta': 			['Dobreta', 	'Mehadia', 			'Craiova'	],
	'Rimnicu Vilcea': 	['Pitesti', 	'Craiova', 			'Sibiu'		],
	'Bucharest': 		['Urziceni', 	'Giurgiu', 			'Pitesti', 		'Fagaras'			],
	'Sibiu': 			['Oradea', 		'Fagaras', 			'Arad', 		'Rimnicu Vilcea'	],
}


def get_best_neighbour(city):
	smallest_distance = 99999
	best_neighbour = None
	for city in neighbours[city]:
		if dist[city] < smallest_distance:
			smallest_distance = dist[city]
			best_neighbour = city
	return best_neighbour


def find_best_path(starting_city, ending_city):
	current_city = starting_city
	if current_city == ending_city:
		print("Destination reached!")
	else:
		next_city = get_best_neighbour(current_city)
		print("\t", next_city)
		find_best_path(next_city, ending_city)


def main():

	starting_city = "Arad"
	ending_city = "Bucharest"

	print("Starting travel from", starting_city)
	find_best_path(starting_city, ending_city)
	print("Travel ended in", ending_city)


if __name__ == "__main__":
	main()