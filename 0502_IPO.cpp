#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        priority_queue<int, vector<int>, less<int>> pq;
        vector<pii> arr;
        for (int i = 0; i < n; ++i) {
            arr.push_back({capital[i], profits[i]});
        }
        sort(arr.begin(), arr.end());
        int curr = 0;
        for (int i = 0; i < k; ++i) {
            while(curr < n && arr[curr].first <= w) {
                pq.push(arr[curr].second);
                ++curr;
            }
            if(!pq.empty()) {
                w += pq.top();
                pq.pop();
            }else{
                break;
            }
        }
        return w;
    }
};

int main() {
    int k = 2, w = 0;
    vector<int> profits{1, 2, 3}, capital{0, 1, 1};
    Solution s;
    cout << s.findMaximizedCapital(k, w, profits, capital) << endl;
}
