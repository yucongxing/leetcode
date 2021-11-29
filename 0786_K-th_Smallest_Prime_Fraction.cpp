#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n = arr.size();
        auto cmp = [&](const pair<int, int> &x, const pair<int, int> &y) {return arr[x.first] * arr[y.second] > arr[x.second] * arr[y.first];};
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> q(cmp);
        for (int i = 1; i < n; ++i) {
            q.push({0, i});
        }
        for (int i = 1; i < k; ++i) {
            auto p = q.top();
            q.pop();
            if (p.first + 1 < p.second) {
                q.push({p.first + 1, p.second});
            }
        }
        return {arr[q.top().first], arr[q.top().second]};
    }
};

int main() {
    Solution s;
    vector<int> v{1, 2, 3, 5};
    int k = 3;
    auto ans = s.kthSmallestPrimeFraction(v, k);
    for (auto &&a : ans) cout << a;
    return 0;
}
