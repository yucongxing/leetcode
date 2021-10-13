#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) dp[i][i] = 1;

        string ans = s.substr(0, 1);
        int tmax = 1;
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    if (i + 1 == j) dp[i][j] = 1;
                    else dp[i][j] = dp[i+1][j-1];
                }
                if (dp[i][j] && j - i + 1 > tmax) {
                    tmax = j - i + 1;
                    ans = s.substr(i, tmax);
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.longestPalindrome("babad") << endl;
    cout << s.longestPalindrome("cbbd") << endl;
    cout << s.longestPalindrome("ac") << endl;
    return 0;
}
