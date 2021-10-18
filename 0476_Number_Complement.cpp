#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int findComplement(int num) {
        bool flag = false;
        int ans = 0;
        for (int i = 31; i >= 0; i--) {
            int x = 1 << i;
            if (x & num) flag = true;
            if (flag) {
                if (x & num) continue;
                else ans ^= x;
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.findComplement(5) << endl;
    return 0;
}
