
# 7	#      (A)--(B)--(C)--(D)
# 	# 	    |              |
# 6	# 	   (E)--(F)       (G)--(H)
# 	# 		     |              |
# 5	# (I)--(J)--(K)--(L)  (M)--(N)--(O)
# 	#  |              |    |         |
# 4	# (P)--(Q)       (R)  (S)       (T)
# 	# 	    |              |         |
# 3	# 	   (U)--(V)       (W)--(X)  (Y)
# 	# 	         |              |    |
# 2	# 	        (Z)       (1)--(2)  (3)
# 	# 		     |                   |
# 1	# 		    (4)--(5)--(6)--(7)--(8)

#      1    2    3    4    5    6    7

import math

nodes_cords = {
    "A" : [2,7],    "B" : [3,7],
    "C" : [4,7],    "D" : [5,7],
    "E" : [2,6],    "F" : [3,6],
    "G" : [5,6],    "H" : [6,6],
    "I" : [1,5],    "J" : [2,5],
    "K" : [3,5],    "L" : [4,5],
    "M" : [5,5],    "N" : [6,5],
    "O" : [7,5],    "P" : [1,4],
    "Q" : [2,4],    "R" : [4,4],
    "S" : [5,4],    "T" : [7,4],
    "U" : [2,3],    "V" : [3,3],
    "W" : [5,3],    "X" : [6,3],
    "Y" : [7,5],    "Z" : [3,2],
    "1" : [5,2],    "2" : [6,2],
    "3" : [7,2],    "4" : [3,1],
    "5" : [4,1],    "6" : [5,1],
    "7" : [6,1],    "8" : [7,1]
}

nodes = {
	"A" : {"B", "E"},   "B" : {"A", "C"},
    "C" : {"B", "D"},   "D" : {"C", "G"},
    "E" : {"A", "F"},   "F" : {"E", "K"},
    "G" : {"D", "H"},   "H" : {"G", "N"},
    "I" : {"J", "P"},   "J" : {"I", "K"},
    "K" : {"J", "L"},   "L" : {"K", "R"},
    "M" : {"N", "S"},   "N" : {"M", "O"},
    "O" : {"N", "T"},   "P" : {"I", "Q"},
    "Q" : {"P", "U"},   "R" : {"L"},
    "S" : {"M", "W"},   "T" : {"O", "Y"},
	"U" : {"Q", "V"},   "V" : {"U", "Z"},
	"W" : {"S", "X"},	"X" : {"W", "2"},
	"Y" : {"T", "3"},	"Z" : {"V", "4"},
	"1" : {"2"},	    "2" : {"1", "X"},
	"3" : {"Y", "8"},	"4" : {"Z", "5"},
	"5" : {"4", "6"},	"6" : {"5", "7"},
	"7" : {"6", "8"},	"8" : {"3", "7"}
}

global begin, end

def get_coordinates(point):
    return nodes_cords[point]

def calculate_distance_from_destination(point , destination):

    # GET COORDINATES
    dest_x, dest_y = get_coordinates(destination)
    point_x, point_y = get_coordinates(point)



    # DIFFERENCES
    diff_x = dest_x - point_x
    diff_y = dest_y - point_y

    # GET LENGTH
    if diff_x < 0:
        diff_x = diff_x * (-1)
    if diff_y < 0:
        diff_y = diff_y * (-1)

    return math.sqrt(diff_x*diff_x + diff_y*diff_y)


def main():
    global begin, end
    begin = "C"
    end = "5"

    print(get_coordinates("V"))
    print( calculate_distance_from_destination("I", "5") )

    pass

if __name__ == "__main__":
    main()