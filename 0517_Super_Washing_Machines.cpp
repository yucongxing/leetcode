#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <numeric>
using namespace std;
typedef long long ll;

class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        int n = machines.size();
        int total = accumulate(machines.begin(), machines.end(), 0);
        if (total % n != 0) return -1;
        int avg = total / n;
        int sum = 0, num = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            num = machines[i] - avg;
            sum += num;
            ans = max({ans, abs(sum), num});
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> machines{0, 3, 0};
    cout << s.findMinMoves(machines) << endl;
    return 0;
}
