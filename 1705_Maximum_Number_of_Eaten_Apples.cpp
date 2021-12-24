#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;
typedef long long ll;

class Solution {
public:
    int eatenApples(vector<int> &apples, vector<int> &days) {
        int n = apples.size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        int ans = 0;
        int begin = n;
        for (int i = 0; i < n; ++i) {
            while (!q.empty() && q.top().first <= i) q.pop();
            if (apples[i] > 0) q.emplace(i + days[i], apples[i]);
            if (!q.empty()) {
                auto t = q.top();
                q.pop();
                ans++;
                if (t.second > 1) q.emplace(t.first, t.second - 1);
            }
        }

        while (!q.empty()) {
            auto t = q.top();
            // cout << t.first << t.second << endl;
            q.pop();
            if (t.first <= begin) continue;
            int cur = min(t.first - begin, t.second);
            ans += cur;
            begin += cur;
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> apples{1, 2, 3, 5, 2}, days{3, 2, 1, 4, 2};
    cout << s.eatenApples(apples, days) << endl;
    vector<int> apples1{3, 0, 0, 0, 2}, days1{3, 0, 0, 0, 2};
    cout << s.eatenApples(apples1, days1) << endl;
    return 0;
}
