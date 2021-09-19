#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int getMaxfac(int n) {
        if (n == 1) return 1;
        int res = 1;
        for (int i = n - 1; i > 1; i--) {
            if (n % i == 0) {
                res = i;
                break;
            }
        }
        return res;
    }

    int minSteps(int n) {
        if (n == 1) return 0;
        int ans = 0;
        int maxfac = getMaxfac(n);
        while(maxfac != 1) {
            ans += n / maxfac;
            cout << ans << endl;
            n = maxfac;
            maxfac = getMaxfac(maxfac);
        }
        ans += n;
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.minSteps(18) << endl;
}
