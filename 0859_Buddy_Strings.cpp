#include <string>
using std::string;
class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.length() != goal.length()) return false;
        int cnt = 0;
        std::pair<char, char> a, b;
        int re[26] = {0,};
        bool flag = false;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == goal[i]) {
                re[s[i] - 'a']++;
                if (re[s[i] - 'a'] > 1) flag = true;
            }
            else {
                ++cnt;
                if (cnt > 2) return false;
                else if(cnt == 1) a = {s[i], goal[i]};
                else b = {s[i], goal[i]};
            }
        }
        if (cnt == 0) {
            return flag;
        }
        return a.first == b.second && a.second == b.first;
    }
};
