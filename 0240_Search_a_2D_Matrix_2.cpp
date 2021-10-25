#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int r = 0, c = n - 1;
        while (r <= m - 1 && c >= 0) {
            int cur = matrix[r][c];
            if (target < cur) {
                --c;
            }else if (target > cur) {
                ++r;
            }else return true;
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<vector<int>> matrix{{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}};
    cout << s.searchMatrix(matrix, 5) << endl;
    return 0;
}
