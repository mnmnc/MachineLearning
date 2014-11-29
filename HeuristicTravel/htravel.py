
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
	'Dobreta': 			['Mehadia', 			'Craiova'	],
	'Rimnicu Vilcea': 	['Pitesti', 	'Craiova', 			'Sibiu'		],
	'Bucharest': 		['Urziceni', 	'Giurgiu', 			'Pitesti', 		'Fagaras'			],
	'Sibiu': 			['Oradea', 		'Fagaras', 			'Arad', 		'Rimnicu Vilcea'	]
}

neighbours_ = {
	'Giurgiu': 		    {'Bucharest':90},
	'Fagaras':			{'Bucharest':211,'Sibiu':99},
	'Lugoj': 			{'Timisoara':111,'Mehadia':70},
	'Mehadia': 			{'Dobreta':75,'Lugoj':70},
	'Oradea': 			{'Zerind':71,'Sibiu':151},
	'Timisoara': 		{'Arad':118,'Lugoj':111},
	'Zerind':			{'Arad':75,'Oradea':71},
	'Arad': 			{'Zerind':75,'Timisoara':118,'Sibiu':140},
	'Craiova': 			{'Dobreta':120,'Rimnicu Vilcea':146,'Pitesti':138},
	'Pitesti': 			{'Bucharest':101,'Rimnicu Vilcea':97,'Craiova':138},
	'Dobreta': 			{'Mehadia':75,'Craiova':120},
	'Rimnicu Vilcea': 	{'Pitesti':97,'Craiova':146,'Sibiu':80},
	'Bucharest': 		{'Urziceni':85,'Giurgiu':90,'Pitesti':101,'Fagaras':211},
	'Sibiu': 			{'Oradea':151,'Fagaras':99,'Arad':140,'Rimnicu Vilcea':80}
}

global previous_city

def get_best_neighbour(city):
	smallest_distance = 99999
	best_neighbour = None
	for city in neighbours[city]:
		if dist[city] < smallest_distance:
			smallest_distance = dist[city]
			best_neighbour = city
	return best_neighbour

def get_best_neighbour_(city):
	global previous_city
	smallest_distance = 99999
	best_neighbour = None
	for local_city in neighbours[city]:
		if local_city == previous_city:
			continue
		distance_from_destination = dist[local_city]
		road_len = neighbours_[city][local_city]
		#print(local_city ,distance_from_destination, road_len, (distance_from_destination-road_len))
		#print(local_city ,distance_from_destination, road_len, (distance_from_destination/road_len))
		if smallest_distance > (distance_from_destination/road_len):
			smallest_distance = distance_from_destination/road_len
			best_neighbour = local_city
	return best_neighbour


def find_best_path(starting_city, ending_city, ):

	current_city = starting_city
	if current_city == ending_city:
		print("Destination reached!")
	else:
		#next_city = get_best_neighbour(current_city)
		next_city = get_best_neighbour_(current_city)
		#get_best_neighbour_(current_city)
		print("\t", next_city)
		previous_city = next_city
		find_best_path(next_city, ending_city)


def main():
	global previous_city
	starting_city = "Arad"
	previous_city = starting_city
	ending_city = "Bucharest"

	print("Starting travel from", starting_city)
	find_best_path(starting_city, ending_city)
	print("Travel ended in", ending_city)


if __name__ == "__main__":
	main()