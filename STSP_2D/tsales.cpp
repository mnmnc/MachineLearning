#include <iostream>
#include <map>
#include <vector>
#include <stdlib.h>
#include <stdio.h>

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



int main(){

	map<string, vector<int> > mapa = build_data_map();

	
	for (map<string, vector<int> >::iterator it = mapa.begin(); it != mapa.end(); ++it ){
		cout << it->first << endl;
	}



	return 0;
} 
