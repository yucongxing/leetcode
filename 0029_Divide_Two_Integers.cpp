#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
using namespace std;
typedef long long ll;

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0) return 0;
        if (dividend == INT_MIN) {
            if (divisor == -1) return INT_MAX;
            if (divisor == 1) return INT_MIN;
        }
        if (divisor == INT_MIN) return dividend == INT_MIN ? 1 : 0;

        bool flag = false;
        if (dividend > 0) {
            dividend = -dividend;
            flag = !flag;
        }
        if (divisor > 0) {
            divisor = -divisor;
            flag = !flag;
        }

        int ans = 0;
        constexpr int LIMIT = -1073741824;
        while (dividend <= divisor) {
            int c = divisor, d = 1;
            while(c > LIMIT && d >= LIMIT && c > dividend - c) {
                c += c;
                d += d;
            }
            ans += d;
            dividend -= c;
        }

        return flag ? -ans : ans;
    }
};

int main() {
    Solution s;
    cout << s.divide(1234, 12) << endl;
    cout << 1234 / 12 << endl;
    return 0;
}
