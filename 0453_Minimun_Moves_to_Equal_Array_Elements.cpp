#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
using namespace std;
typedef long long ll;

class Solution {
public:
    int minMoves(vector<int> &nums) {
        ll min = INT_MAX, sum = 0;
        for (auto&& num : nums) {
            sum += num;
            if (num < min) {
                min = num;
            }
        }
        return sum - min * nums.size();
    }
};

int main() {
    Solution s;
    return 0;
}
