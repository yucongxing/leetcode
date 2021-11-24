#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
using namespace std;
typedef long long ll;

class Solution {
public:
    int maxProduct(vector<int> &nums) {
        int n = nums.size();
        vector<int> maxdp(n, 0), mindp(n, 0);
        maxdp[0] = nums[0];
        mindp[0] = nums[0];
        int ans = nums[0];
        for (int i = 1; i < n; ++i) {
            maxdp[i] = max(max(maxdp[i - 1] * nums[i], nums[i]), mindp[i - 1] * nums[i]);
            mindp[i] = min(min(maxdp[i - 1] * nums[i], nums[i]), mindp[i - 1] * nums[i]);
            ans = max(ans, maxdp[i]);
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> v{2, 3, -2, 4};
    cout << s.maxProduct(v) << endl;
    return 0;
}
