#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <functional>
using namespace std;
typedef long long ll;

class Solution {
public:
    int trapRainWater(vector<vector<int>> &heightMap){
        auto cmp = [] (tuple<int, int, int> &a, tuple<int, int, int> &b) {return get<2>(a) > get<2>(b);};
        priority_queue<tuple<int, int ,int>, vector<tuple<int, int, int>>, function<bool(tuple<int, int, int>&, tuple<int, int, int >&)>> q(cmp);
        int m = heightMap.size(), n = heightMap[0].size();
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        for (int i = 0; i < n; ++i) {
            q.push(make_tuple(0, i, heightMap[0][i]));
            vis[0][i] = true;
            q.push(make_tuple(m - 1, i, heightMap[m - 1][i]));
            vis[m - 1][i] = true;
        }
        for (int i = 1; i < m - 1; ++i) {
            q.push(make_tuple(i, 0, heightMap[i][0]));
            vis[i][0] = true;
            q.push(make_tuple(i, n - 1, heightMap[i][n - 1]));
            vis[i][n - 1] = true;
        }
        vector<vector<int>> dir{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int ans = 0;
        while (!q.empty()) {
            int curx, cury, h;
            tie(curx, cury, h) = q.top();
            q.pop();
            for (auto&& d : dir) {
                int nx = curx + d[0];
                int ny = cury + d[1];
                if (nx >=0 && nx < m && ny >= 0 && ny < n && !vis[nx][ny]) {
                    if (heightMap[nx][ny] < h) {
                        ans += h - heightMap[nx][ny];
                    }
                    q.push(make_tuple(nx, ny, max(h, heightMap[nx][ny])));
                    vis[nx][ny] = true;
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    return 0;
}
