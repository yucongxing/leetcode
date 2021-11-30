#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
typedef long long ll;

class Solution {
public:
    int findNthDigit(int n) {
        if (n < 10) return n;
        int num = 1;
        int sum = 0;
        for (int i = 1; i <= 10; ++i) {
            if (sum + i * 9 * pow(10, i - 1) < n) {
                sum += i * 9 * pow(10, i - 1);
                num = i;
                cout << sum << endl;
            }else {
                break;
            }
        }
        n -= sum;
        int x = n / (num + 1);
        int digit = n % (num + 1);
        cout << x << " " << digit << endl;
        int ans = (int)(pow(10, num) + x - 1);
        cout << "ans: " << ans << endl;
        if (digit) {
            ans += 1;
            return to_string(ans)[digit - 1] - '0';
        }else {
            return to_string(ans).back() - '0';
        }
    }
};

int main() {
    Solution s;
    cout << s.findNthDigit(10) << endl;
    cout << s.findNthDigit(11) << endl;
    cout << s.findNthDigit(190) << endl;
    cout << s.findNthDigit(2890) << endl;
    return 0;
}
