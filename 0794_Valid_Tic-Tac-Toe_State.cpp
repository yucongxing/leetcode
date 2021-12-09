#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool validTicTacToe(vector<string> &board) {
        int xcnt{0}, ocnt{0};
        for (auto && s : board) {
            for (auto &&ch : s) {
                if (ch == 'X') {
                    xcnt++;
                }else if (ch == 'O') {
                    ocnt++;
                }
            }
        }
        if (xcnt - ocnt > 1 || xcnt - ocnt < 0) return false;
        bool xwin{false}, owin{false};
        for (int i = 0; i < 3; ++i) {
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
                if (board[i][0] == 'X') xwin = true;
                else if (board[i][0] == 'O') owin = true;
            }
            if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
                if (board[0][i] == 'X') xwin = true;
                else if (board[0][i] == 'O') owin = true;
            }
        }
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
                if (board[0][0] == 'X') xwin = true;
                else if (board[0][0] == 'O') owin = true;
        }
        if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
                if (board[0][2] == 'X') xwin = true;
                else if (board[0][2] == 'O') owin = true;
        }
        if (xwin && owin) return false;
        if (xwin) return xcnt - ocnt == 1;
        if (owin) return xcnt == ocnt;
        return true;
    }
};

int main() {
    Solution s;
    return 0;
}
