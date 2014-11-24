
distance = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Lugoj': 244,
    'Mehadia': 241,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Zerind': 374
}

neighbours = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Bucharest': ['Urziceni', 'Giurgiu', 'Pitesti', 'Fagaras'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Dobreta': ['Dobreta', 'Mehadia', 'Craiova'],
    'Fagaras': ['Bucharest', 'Sibiu'],
    'Giurgiu': ['Bucharest'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Dobreta', 'Lugoj'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Pitesti': ['Bucharest', 'Rimnicu Vilcea', 'Craiova'],
    'Rimnicu Vilcea': ['Pitesti', 'Craiova', 'Sibiu'],
    'Sibiu': ['Oradea', 'Fagaras', 'Arad', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Zerind': ['Arad', 'Oradea']
}
