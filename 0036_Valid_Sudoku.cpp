#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> inum(9, 0), jnum(9, 0);
        vector<vector<int>> snum(3, vector<int>(3, 0));
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++){
                if (board[i][j] == '.') continue;

                int x = board[i][j] -'0';

                if (inum[i] & (1 << x) || jnum[j] & (1 << x) && snum[i / 3][j / 3] & (1 << x)) return false;

                inum[i] ^= (1 << x);
                jnum[j] ^= (1 << x);
                snum[i / 3][j / 3] ^= (1 << x);
            }
        }
        return true;
    }
};

int main() {
    Solution s;
    return 0;
}
