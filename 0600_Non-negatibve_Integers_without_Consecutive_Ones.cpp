#include <iostream>
using namespace std;

class Solution {
public:
    int findIntegers(int n) {
        int dp[31][2];
        dp[1][0] = 1;
        dp[1][1] = 2;
        for (int i = 1; i < 30; ++i) {
            dp[i + 1][0] = dp[i][1];
            dp[i + 1][1] = dp[i][0] + dp[i][1];
        }

        int len = 31;
        while((n & (1 << len)) == 0) --len;
        int ans = 0, pre = 0;
        for (int i = len; i >= 0; --i) {
            int cur = ((n >> i) & 1);
            if (cur == 1) ans += dp[i + 1][0];
            if (cur == 1 && pre == 1) break;
            pre = cur;
            if (i == 0) ++ans;
        }
        return ans;
        return 0;
    }
};

int main() {
    Solution s;
    cout << s.findIntegers(5) << endl;
}
