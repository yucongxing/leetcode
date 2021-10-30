#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<int> singleNumber(vector<int> &nums) {
        int x = 0;
        for (auto &&num : nums) {
            x ^= num;
        }
        // int mask = x == INT_MIN ? x : x & (-x); //get the last '1'
        int mask = 1;
        while ((mask & x) == 0) {
            mask <<= 1;
        }
        int a1 = 0, a2 = 0;
        for (auto && num : nums) {
            if (num & mask) {
                a1 ^= num;
            }else {
                a2 ^= num;
            }
        }
        return {a1, a2};
    }
};

int main() {
    Solution s{};
    vector<int> nums{1, 2, 1, 3, 2, 5};
    vector<int> ans = s.singleNumber(nums);
    for (auto a : ans) cout << a << endl;
    return 0;
}
