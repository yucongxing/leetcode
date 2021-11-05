#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
typedef long long ll;

class Solution {
public:
    int longestSubsequence(vector<int> &arr, int difference) {
        unordered_map<int, int> dp;
        int ans{0};
        for (auto &&a : arr) {
            dp[a] = dp[a - difference] + 1;
            ans = max(ans, dp[a]);
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> arr{1, 2, 3, 4};
    cout << s.longestSubsequence(arr, 1) << endl;
    return 0;
}
