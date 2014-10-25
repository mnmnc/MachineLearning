point_a = [ 1, 4, 4 ];
point_b = [ 1, 5, 5 ];
point_c = [ 1, 6, 5 ];
point_d = [ 0, 1, 3 ];
point_e = [ 0, 2, 6 ];

points = [ point_a, point_b, point_c, point_d, point_e ]
hipothesis = [ ]

def show_hipo():
    for limit in hipothesis:
        print( limit );

def initialize_hipothesis():
    global hipothesis
    hipothesis = [ points[0][1], points[0][1], points[0][2], points[0][2] ]

def calculate():
    for point in points:
        if point[0] == 1:
            if point[1] < hipothesis[0] : hipothesis[0] = point[1];
            if point[1] > hipothesis[1] : hipothesis[1] = point[1];
            if point[2] < hipothesis[2] : hipothesis[2] = point[2];
            if point[2] > hipothesis[3] : hipothesis[3] = point[2];

def main():
    initialize_hipothesis();
    calculate();
    show_hipo();

if __name__ == "__main__":
    main();