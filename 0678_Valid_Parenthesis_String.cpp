#include <stack>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool checkValidString(string s) {
        int min = 0, max = 0;
        for (auto ch : s) {
            if (ch == '(') {
                min++;
                max++;
            }else if (ch == ')') {
                min = min - 1 < 0 ? 0 : min - 1;
                max--;
                if (max < 0) return false;
            }else{
                min = min - 1 < 0 ? 0 : min - 1;
                max++;
            }
        }
        return min == 0;
    }
};

int main() {
    Solution s;
    string str = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())";
    cout << s.checkValidString(str) << endl;
}
// 括号匹配
