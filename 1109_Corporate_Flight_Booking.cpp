#include <vector>
#include <iostream>
#include <numeric>
#include <iterator>
using namespace std;

class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> ans(n);
        for (auto booking : bookings) {
            ans[booking[0] - 1] += booking[2];
            if (booking[1] < n) {
                ans[booking[1]] -= booking[2];
            }
        }
        vector<int> presum;
        partial_sum(ans.begin(), ans.end(), back_inserter(presum));
        return presum;
    }
};

int main() {
    Solution s;
    vector<vector<int>> bookings{{1, 2, 10}, {2, 3, 20}, {2, 5, 25}};
    vector<int> ans = s.corpFlightBookings(bookings, 5);
    for (auto a : ans) {
        cout << a << endl;
    }
}
