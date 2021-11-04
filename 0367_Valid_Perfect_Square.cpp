#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool isPerfectSquare(int num) {
        /* 二分
        int l = 1, r = num;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if ((long)mid * mid > num) {
                r = mid - 1;
            }else if ((long)mid * mid < num) {
                l = mid + 1;
            }else {
                return true;
            }
        }
        return false;
        */
        double x0 = num;
        double d = 1e-12;
        while (abs(x0 * x0 - num) > d) {
            x0 = (x0 + num / x0) / 2;
        }
        int sq = (int) x0;
        return sq * sq == num;
    }
};

int main() {
    Solution s;
    cout << s.isPerfectSquare(9) << endl;
    return 0;
}
