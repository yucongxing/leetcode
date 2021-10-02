#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    string toHex(int num) {
        if (num == 0) return "0";
        char toh[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
        unsigned int m = (unsigned)num;
        string ans = "";
        while (m) {
            ans = toh[m % 16] + ans;
            m /= 16;
        }
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.toHex(26) << endl;
    return 0;
}
