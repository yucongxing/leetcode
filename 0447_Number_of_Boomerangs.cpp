#include <vector>
#include <iostream>
#include <unordered_map>
#include <map>
using namespace std;

typedef long long ll;

struct pairHash {
    template<class T1, class T2>
    size_t operator()(const pair<T1, T2> &p) const {
        size_t seed = 0;
        seed ^= hash<T1>()(p.first) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        seed ^= hash<T2>()(p.second) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        return seed;
    }
};

class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int n = points.size();
        unordered_map<pair<int, int>, int, pairHash> dist;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                pair<int, int> p{i, j};
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                dist[p] = dx * dx + dy * dy;
            }
        }
        ll ans = 0;
        for(int i = 0; i < n; ++i) {
            unordered_map<int, int> re;
            for(int j = 0; j < n; ++j) {
                if (i != j) {
                    int t1 = 0, t2 = 0;
                    if (i < j) t1 = i, t2 = j;
                    else t1 = j; t2 = i;
                    pair<int, int> p{move(t1), move(t2)};
                    re[dist[p]]++;
                }
            }
            for (auto &it : re) {
                if (it.second >= 2) ans += it.second * (it.second - 1);
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<vector<int>> points{{0, 0}, {1, 0}, {2, 0}};
    cout << s.numberOfBoomerangs(points) << endl;
}
// 447 pairHash so slow...
