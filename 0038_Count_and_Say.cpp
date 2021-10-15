#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        string s = "11";
        for (int l = 0; l < n - 2; l++) {
            s += "#";
            string t = "";
            char cur = s[0];
            int cnt = 1, len = s.length();
            for (int i = 1; i < len; i++) {
                if (s[i] != s[i - 1]) {
                    t += to_string(cnt);
                    t.push_back(cur);
                    cur = s[i];
                    cnt = 1;
                }else {
                    cnt++;
                }
            }
            cout << t << endl;
            s = t;
        }
        return s;
    }
};

int main() {
    Solution s{};
    cout << s.countAndSay(30) << endl;
    return 0;
}
