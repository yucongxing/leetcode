#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int bitProcess(bool x, bool y, bool z) {
        int res = 0;
        if (x) res ^= 1;
        if (y) res ^= (1 << 1);
        if (z) res ^= (1 << 2);
        return res;
    }

    int getSum(int a, int b) {
        int len = 32;
        int flag = 0;
        int res = 0;
        for (int i = 0; i < len; i++) {
            cout << res << endl;
            int cur = 1 << i;
            int bit_num = bitProcess((cur & a), (cur & b), flag);
            if (bit_num == 7) {
                res ^= cur;
                flag = 1;
            }else if (bit_num == 3 || bit_num == 5 || bit_num == 6) {
                flag = 1;
            }else if (bit_num == 4 || bit_num == 2 || bit_num == 1) {
                res ^= cur;
                flag = 0;
            }else {
                flag = 0;
            }
        }
        return res;
    }
    /* pretty solution
    int getSum(int a, int b) {
        while (b != 0) {
            unsigned int carry = (unsigned int)(a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
    */
};

int main() {
    Solution s;
    int a = 2, b = 3;
    cout << s.getSum(a, b) << endl;
    return 0;
}
