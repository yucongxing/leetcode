#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
using namespace std;
typedef long long ll;

class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> dp(n+1, vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 1; --i) {
            for (int j = i + 1; j <= n; ++j) {
                int minM = INT_MAX;
                for (int k = i; k < j; ++k) {
                    int cur = k + max(dp[i][k - 1], dp[k + 1][j]);
                    minM = min(minM, cur);
                }
                dp[i][j] = minM;
            }
        }
        return dp[1][n];
    }
};

int main() {
    Solution s;
    cout << s.getMoneyAmount(10) << endl;
    return 0;
}
