#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int findLHS(vector<int> &nums) {
        map<int, int> m;
        for (auto &&n : nums) {
            m[n]++;
        }
        int ans = 0;
        for (auto &&p : m) {
            if (m.find(p.first + 1) != m.end()) {
                ans = max(ans, p.second + m[p.first + 1]);
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    return 0;
}
