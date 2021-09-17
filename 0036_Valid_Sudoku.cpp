#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> inum(9, 0), jnum(9, 0), snum(9, 0);
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++){
                cout << board[i][j] << endl;
                int x = board[i][j] -'0';
                if (inum[i] & (1 << x)) return false;
                else inum[i] ^= (1 << x);
                if (jnum[j] & (1 << x)) return false;
                else jnum[j] ^= (1 << x);
                if(i / 3 == 0 && j / 3 == 0) {
                    if (snum[0] & (1 << x)) return false;
                    else snum[0] ^= (1 << x);
                }else if(i / 3 == 1 && j / 3 == 0) {
                    if (snum[1] & (1 << x)) return false;
                    else snum[1] ^= (1 << x);
                }else if(i / 3 == 2 && j / 3 == 0) {
                    if (snum[2] & (1 << x)) return false;
                    else snum[2] ^= (1 << x);
                }else if(i / 3 == 0 && j / 3 == 1) {
                    if (snum[3] & (1 << x)) return false;
                    else snum[3] ^= (1 << x);
                }else if(i / 3 == 1 && j / 3 == 1) {
                    if (snum[4] & (1 << x)) return false;
                    else snum[4] ^= (1 << x);
                }else if(i / 3 == 2 && j / 3 == 1) {
                    if (snum[5] & (1 << x)) return false;
                    else snum[5] ^= (1 << x);
                }else if(i / 3 == 0 && j / 3 == 2) {
                    if (snum[6] & (1 << x)) return false;
                    else snum[6] ^= (1 << x);
                }else if(i / 3 == 1 && j / 3 == 2) {
                    if (snum[7] & (1 << x)) return false;
                    else snum[7] ^= (1 << x);
                }else{
                    if (snum[8] & (1 << x)) return false;
                    else snum[8] ^= (1 << x);
                }
            }
        }
        return true;
    }
};

int main() {
    Solution s;
    return 0;
}
