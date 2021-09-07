#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int balancedStringSplit(string s) {
        int lcnt(0), rcnt(0), ans(0);
        for (auto c : s) {
            if (c == 'L') {
                lcnt++;
            }else rcnt++;
            if (lcnt == rcnt) {
                ans++;
                lcnt = rcnt = 0;
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    string str = "RLRRLLRLRL";
    cout << s.balancedStringSplit(str) << endl;
}

