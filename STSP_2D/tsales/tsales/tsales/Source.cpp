#include <iostream>
#include <map>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <string>

// mini_map = {
// 	"AA": {"x": 0, "y": 13},
// 	"AB": {"x": 0, "y": 26},
// 	"AC": {"x": 0, "y": 27},
// 	"AD": {"x": 0, "y": 39},
// 	"AE": {"x": 2, "y": 0},
// 	"AF": {"x": 5, "y": 13},
// 	"AG": {"x": 5, "y": 19},
// 	"AH": {"x": 5, "y": 25},
// 	"AI": {"x": 5, "y": 31},
// 	"AJ": {"x": 5, "y": 37}
// }


using namespace std;

map<string, vector<int> > build_data_map(){

	vector<int> point;
	map<string, vector<int> > mapa;

	point.push_back(0);
	point.push_back(13);
	mapa["AA"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(26);
	mapa["AB"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(27);
	mapa["AC"] = point;
	point.clear();

	point.push_back(0);
	point.push_back(39);
	mapa["AD"] = point;
	point.clear();

	point.push_back(2);
	point.push_back(0);
	mapa["AE"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(13);
	mapa["AF"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(19);
	mapa["AG"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(25);
	mapa["AH"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(31);
	mapa["AI"] = point;
	point.clear();

	point.push_back(5);
	point.push_back(37);
	mapa["AJ"] = point;
	point.clear();

	return mapa;
}

vector<string> get_nodes(map<string, vector<int> > mapa){
	vector<string> result;
	for (map<string, vector<int> >::iterator it = mapa.begin(); it != mapa.end(); ++it){
		result.push_back(it->first);
	}
	return result;
}

double get_distance(string s1, string s2, map<string, vector<int> > mapa){
	int x1 = mapa[s1].at(0);
	int y1 = mapa[s1].at(1);
	int x2 = mapa[s2].at(0);
	int y2 = mapa[s2].at(1);


}

void print_vector(vector<string> vec){
	for (int i = 0; i < vec.size(); ++i){
		cout << "[" << i << "] = " << vec.at(i) << endl;
	}
}



int main(){

	map<string, vector<int> > mapa = build_data_map();

	print_vector(get_nodes(mapa));


	system("PAUSE");
	return 0;
}
