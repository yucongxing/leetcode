#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int geta(char c) {
        if (c == '*') return 9;
        else if (c == '0') return 0;
        else return 1;
    }
    int getb(char c1, char c2) {
        if (c1 == '0') return 0;
        if (c1 == '*' && c2 == '*') {
            return 15;
        }else if (c2 == '*') {
            if (c1 - '0' == 1) return 9;
            else if(c1 - '0' == 2) return 6;
            else return 0;
        }else if (c1 == '*') {
            if (c2 - '0' <= 6) return 2;
            else return 1;
        }else {
            int cur = (c1 - '0') * 10 + c2 - '0';
            if (cur <= 26) return 1;
            else return 0;
        }
    }
    int numDecodings(string s) {
        if (s[0] == '0') return 0;
        const int mod = 1e9 + 7;
        int n = s.length();
        ll first = 1, secend = s[0] == '*' ? 9 : 1;
        ll ans = secend;
        for (int i = 1; i < n; i++) {
            int a = geta(s[i]), b = getb(s[i-1], s[i]);
            ans = ((a * secend % mod) + (b * first % mod)) % mod;
            first = secend;
            secend = ans;
        }
        return (int)ans;
    }
};

int main() {
    Solution s;
    string str = "904";
    cout << s.numDecodings(str) << endl;
    return 0;
}
