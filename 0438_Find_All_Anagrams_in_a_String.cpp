#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool compare(int a[], int b[]) {
        for (int i = 0; i < 26; ++i) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }

    vector<int> findAnagrams(string s, string p) {
        int sLen = s.length(), pLen = p.length();

        vector<int> ans{};
        if (sLen < pLen) return ans;

        int sre[26] = {0}, pre[26] = {0};
        for (int i = 0; i < pLen; ++i) {
            sre[s[i] - 'a']++;
            pre[p[i] - 'a']++;
        }

        if (compare(pre, sre)) ans.push_back(0);

        for (int i = pLen; i < sLen; ++i) {
            sre[s[i] - 'a']++;
            sre[s[i - pLen] - 'a']--;
            if (compare(pre, sre)) ans.push_back(i - pLen + 1);
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> ans = s.findAnagrams("cbaebabacd", "abc");
    for (auto && ch : ans) cout << ch;
    return 0;
}
