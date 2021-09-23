#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool isPowerOfThree(int n) {
        while (n / 3 != 0) {
            if (n % 3 != 0) {
                return false;
            }else {
                n /= 3;
            }
        }
        return n == 1;
        //return n > 0 && 1162261467 % n == 0;
    }
};

int main() {
    Solution s;
    cout << s.isPowerOfThree(27) << endl;
    cout << s.isPowerOfThree(0) << endl;
    return 0;
}
