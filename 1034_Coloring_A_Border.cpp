#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<int> direct{-1, 0, 1, 0, -1};
    void dfs(vector<vector<int>> &grid, int row, int col, vector<vector<bool>> &visit, vector<pair<int, int>> &borders) {
        visit[row][col] = true;
        int m = grid.size(), n = grid[0].size();
        for (int i = 0; i < 4; ++i) {
            int nextrow = row + direct[i];
            int nextcol = col + direct[i + 1];
            if (nextrow < 0 || nextrow >= m || nextcol < 0 || nextcol >= n || grid[nextrow][nextcol] != grid[row][col]) {
                borders.emplace_back(row, col);
            }else if(!visit[nextrow][nextcol]) {
                dfs(grid, nextrow, nextcol, visit, borders);
            }
        }

    }
    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int row, int col, int color) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visit(m, vector<bool>(n, false));
        vector<pair<int, int>> borders{};
        dfs(grid, row, col, visit, borders);
        for (auto &&b : borders) {
            grid[b.first][b.second] = color;
        }
        return grid;
    }
};

int main() {
    Solution s;
    vector<vector<int>> grid{{1, 1}, {1, 2}};
    vector<vector<int>> ans = s.colorBorder(grid, 0, 0, 3);
    for (auto&& vec : ans) {
        for (auto&& i : vec) {
            cout << i;
        }
        cout << endl;
    }
    return 0;
}
