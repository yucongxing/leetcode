#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <functional>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<string> addOperators(string num, int target) {
        int n = num.length();
        vector<string> ans{};
        function<void(string&, int, long, long)> dfs = [&](string &expr, int i, long res, long mul) {
            if (i == n) {
                if (res == target) {
                    ans.push_back(expr);
                }
                return;
            }

            int signPos = expr.length();

            if (i > 0) {
                expr.push_back('#');
            }

            long val{0};
            for (int j = i; j < n && (j == i || num[i] != '0'); ++j) {
                val = val * 10 + num[j] - '0';
                expr.push_back(num[j]);
                if (i == 0) {
                    dfs(expr, j + 1, val, val);
                }else {
                    expr[signPos] = '+';
                    dfs(expr, j + 1, res + val, val);
                    expr[signPos] = '-';
                    dfs(expr, j + 1, res - val, -val);
                    expr[signPos] = '*';
                    dfs(expr, j + 1, res - mul + mul * val, mul * val);
                }
            }
            expr.resize(signPos);
        };
        string expr{};
        dfs(expr, 0, 0, 0);
        return ans;
    }
};

int main() {
    Solution s;
    vector<string> ans = s.addOperators("123", 6);
    for (auto& ex : ans) {
        cout << ex << '\n';
    }
    return 0;
}
