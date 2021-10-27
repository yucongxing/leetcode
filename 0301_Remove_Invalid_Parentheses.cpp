#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_set>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> ans{};
        auto isValid = [](string ss) {
            int cnt = 0;
            for (auto &&c : ss) {
                if (c == '(') ++cnt;
                else if (c == ')') {
                    --cnt;
                    if (cnt < 0) return false;
                }
            }
            return cnt == 0;
        };

        unordered_set<string> strSet{};
        queue<string> q{};
        int flag = 0;

        q.push(s);

        while (!q.empty()) {
            string cur = q.front();
            if (cur.length() < flag) break;
            q.pop();
            if (isValid(cur)) {
                ans.push_back(cur);
                flag = cur.length();
            }
            if (flag) continue;

            for (int i = 0; i < cur.length(); ++i) {
                if (cur[i] == '(' || cur[i] == ')') {
                    if (i > 0 && cur[i] == cur[i - 1]) continue;
                    string t{};
                    t = cur.substr(0, i) + cur.substr(i + 1, cur.length());
                    if (!strSet.count(t)) {
                        q.push(t);
                        strSet.insert(t);
                    }
                }
            }
        }

        if (ans.size() == 0) {
            ans.push_back("");
        }

        return ans;
    }
};

int main() {
    Solution s;
    string str = "(a)())()";
    vector<string> ans = s.removeInvalidParentheses(str);
    cout << "ans:" << endl;
    for (auto &&a : ans) cout << a << endl;
    return 0;
}
