#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int n = chalk.size();
        vector<int> presum(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            presum[i] = presum[i - 1] + chalk[i - 1];
            if (presum[i] > k) {
                return i - 1;
            }
        }
        k = k % *(presum.end() - 1);
        
        return upper_bound(presum.begin(), presum.end(), k) - presum.begin() - 1;
    }
};

int main() {
    Solution s;
    vector<int> chalk{3, 4, 1, 2};
    int k = 25;
    cout << s.chalkReplacer(chalk, k) << endl;
}
