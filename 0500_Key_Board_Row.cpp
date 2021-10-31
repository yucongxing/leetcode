#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<string> findWords(vector<string> &words) {
        unordered_map<char, int> re{};
        for (auto c : "qwertyuiop") {
            re[c] = 0;
            re[c - 32] = 0;
        }
        for (auto c : "asdfghjkl") {
            re[c] = 1;
            re[c - 32] = 1;
        }
        for (auto c : "zxcvbnm") {
            re[c] = 2;
            re[c - 32] = 2;
        }
        
        vector<string> ans{};
        for (auto && w : words) {
            int cur = re[w[0]];
            bool flag = true;
            for (int i = 1; i < w.length(); ++i) {
                if (re[w[i]] != cur) {
                    flag = false;
                    break;
                }                    
            }
            if (flag) ans.push_back(w);
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<string> words{"Hello", "Alaska", "Dad", "Peace"};
    vector<string> ans = s.findWords(words);
    for (auto &&a : ans) cout << a << endl;
    return 0;
}
