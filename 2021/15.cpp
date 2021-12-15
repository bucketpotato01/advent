#include <algorithm>
#include <array>
#include <cassert>
#include <cstring>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define ll long long
#define n 500
#define INF 99999999999999

int gr[n][n];
vector<pair<int,int>> g[n * n];
ll dist[n * n];
string s[n];

int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};

void dijkstra() {

	set<pair<ll,ll>> curr;
	for (int i = 0; i < n * n; i++)
		curr.insert({dist[i], i});
	while (curr.size()) {

		auto cv = *curr.begin();
		curr.erase(curr.begin());
		int cn = cv.second;
		ll cd = cv.first;

		for (auto [co, i] : g[cn]) {

			if (co + cd < dist[i]) {
				curr.erase(curr.find({dist[i], i}));
				dist[i] = co + cd;
				curr.insert({dist[i], i});
			}

		}

	}

}

int main() {

	ifstream fin("in.txt");
	for (int i = 0; i < n / 5; i++)
		fin >> s[i];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			gr[i][j] = (s[i % (n / 5)][j % (n / 5)] - '0') + (i / (n / 5)) + (j / (n / 5));
			if (gr[i][j] > 9) gr[i][j] -= 9;
			// cout << gr[i][j];
		}
		// cout << endl;
	}


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {

			int cv = (i * n) + j;
			dist[cv] = INF;
			for (int k = 0; k < 4; k++) {

				int nr = i + dr[k];
				int nc = j + dc[k];

				if (nr < 0 || nc < 0) continue;
				if (nr >= n || nc >= n) continue;

				int ov = (nr * n) + nc;

				g[cv].push_back({gr[nr][nc], ov});
			}

		}
	}

	dist[0] = 0;

	dijkstra();

	cout << dist[n * (n - 1) + (n - 1)] << endl;
	
}