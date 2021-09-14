#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        int n = s.length();
        vector<vector<int>> dp(n + 1, vector<int>(26, 0));
        for (int i = 0; i < 26; i++) {
            dp[n][i] = n;
        }
        for (int i = n - 1; i >= 0; i--) {
            for(int j = 0; j < 26; j++) {
                if (s[i] - 'a' == j) {
                    dp[i][j] = i;
                }else {
                    dp[i][j] = dp[i + 1][j];
                }
            }
        }
        string ans = "";
        for (auto& str : dictionary) {
            bool match = true;
            int cur = 0;
            for (auto& ch : str) {
                if (dp[cur][ch - 'a'] == n) {
                    match = false;
                    break;
                }else {
                    cur = dp[cur][ch - 'a'] + 1;
                }
            }
            if (match) {
                if (ans.length() < str.length() || (ans.length() == str.length() && str < ans)){
                    ans = str;
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    string s1 = "abpcplea";
    vector<string> dictionary{"ale", "apple", "monkey", "plea"};
    cout << s.findLongestWord(s1, dictionary) << endl;
}
