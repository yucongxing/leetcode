#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        int len = 0;
        for (auto& c : s) {
            if (c != '-') len++;
            if (islower(c)) c -= 32;
        }
        int remain = len % k, cnt = 0;
        string ans = "";
        for (auto &c : s) {
            if (c != '-') {
                ans.push_back(c);
                cnt++;
                if (cnt == len) break;
                if (cnt == remain || (cnt - remain) % k == 0) {
                    ans.push_back('-');
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.licenseKeyFormatting("5F3Z-2e-9-w", 4) << endl;
    return 0;
}
