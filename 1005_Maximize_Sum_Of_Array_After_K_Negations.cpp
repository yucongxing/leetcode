#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;
typedef long long ll;

class Solution {
public:
    int largestSumAfterKNegations(vector<int> &nums, int k) {
        priority_queue<int, vector<int>, less<int>> pq;
        int nn = 0;
        int sum = 0;
        for (auto &&n : nums) {
            sum += n;
            if (n < 0) ++nn;
            pq.push(n);
        }
        for (int i = 0; i < nn && i < k; ++i) {
            int t = pq.top();
            sum -= 2 * t;
            pq.pop();
            pq.push(t);
        }

        if (k > nn && (k - nn) & 1) sum -= 2 * pq.top();
        return sum;
    }
};

int main() {
    Solution s;
    return 0;
}
