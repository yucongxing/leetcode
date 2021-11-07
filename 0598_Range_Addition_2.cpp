#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>> &ops) {
        int minw = m, minh = n;
        for (auto && op : ops) {
            if (op[0] < minw) {
                minw = op[0];
            }
            if (op[1] < minh) {
                minh = op[1];
            }
        }
        return minw * minh;
    }
};

int main() {
    Solution s;
    return 0;
}
