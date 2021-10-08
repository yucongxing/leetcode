#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        int n = s.length();
        static constexpr int encoder[26] = {0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0};
        vector<string> ans{};

        if (n < 10) return ans;

        int w = 0;
        for (int i = 0; i < 9; i++) {
            w = (w << 2) | encoder[s[i] - 'A'];
        }
        unordered_map<int, int> re;
        for (int i = 9; i < n; i++) {
            w = ((w << 2) | encoder[s[i] - 'A']) & ((1 << 20) -1);
            if (++re[w] == 2) ans.push_back(s.substr(i - 9, 10));
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<string> ans = s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT");
    for (auto &s : ans) {
        cout << s << endl;
    }
    return 0;
}
