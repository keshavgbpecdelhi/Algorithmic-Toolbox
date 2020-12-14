 
// Edit Distance : Problem Introduction
// The edit distance between two strings is the minimum number of operations (insertions, deletions, and
// substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
// Edit distance has applications, for example, in computational biology, natural language processing, and spell
// checking. Your goal in this problem is to compute the edit distance between two strings.
// Problem Description
// Task. The goal of this problem is to implement the algorithm for computing the edit distance between two
// strings.
// Input Format. Each of the two lines of the input contains a string consisting of lower case latin letters.
// Constraints. The length of both strings is at least 1 and at most 100.
// Output Format. Output the edit distance between the given two strings.
// Sample 1.
// Input:
// ab
// ab
// Output:
// 0
// Sample 2.
// Input:
// short
// ports
// Output:
// 3
// An alignment of total cost 3:
// s h o r t −
// − p o r t s
// Sample 3.
// Input:
// editing
// distance
// Output:
// 5
// An alignment of total cost 5:
// e d i − t i n g −
// − d i s t a n c e

/******************************************************************************

Edit Distance : Solution in C++

*******************************************************************************/

#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define endl '\n'

typedef long long int ll;

using namespace std;


int editDistance(string str1, string str2, int m, int n) {
	vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    for (int i = 0; i <= m; i++) {
		for (int j = 0; j <= n; j++) {
			if (i == 0)
				dp[i][j] = j;

			else if (j == 0)
				dp[i][j] = i;

			else if (str1[i - 1] == str2[j - 1])
				dp[i][j] = dp[i - 1][j - 1];

			else
				dp[i][j] = 1 + min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]);
		}
	}

	return dp[m][n];
}

int main() {
	string fs, ss; //first string = fs and second string = ss
	cin >> fs >> ss;
	cout << editDistance(fs, ss, fs.size(),ss.size()) << endl;
}
