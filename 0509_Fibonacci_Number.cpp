#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int fib(int n) {
        if (n == 0 || n == 1) return n;
        if(n == 2) return 1;
        vector<vector<long>> f{{1, 1, 1}, {1, 0, 0}, {0, 1, 0}};
        vector<vector<long>> ans{{1}, {1}, {0}};
        vector<vector<long>> t = pow(f, n - 2);
        ans = product(t, ans);
        return ans[0][0];
    }

private:
    vector<vector<long>> product(vector<vector<long>>& x, vector<vector<long>>& y) {
        int l = x.size(), m = y.size(), n = y[0].size();
        vector<vector<long>> ans(l, vector<long>(n, 0));
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    ans[i][j] += x[i][k] * y[k][j];
                }
            }
        }
        return ans;
    }

    vector<vector<long>> pow(vector<vector<long>>& x, int n) {
        int l = x.size();
        if (n == 1) return x;
        vector<vector<long>> ans(l, vector<long>(l, 0));
        for (int i = 0; i < l; i ++) ans[i][i] = 1;
        while (n) {
            if (n & 1) {
                ans = product(ans, x);
            }
            x = product(x, x);
            n >>= 1;
            // cout << ans[0][0] << ' ' << ans[0][1] << endl;
            // cout << ans[1][0] << ' ' << ans[1][1] << endl;
        }
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.fib(4) << endl;
    cout << s.fib(25) << endl;
    cout << s.fib(8) << endl;
}
