#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
typedef long long ll;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if ((int64_t)numerator % denominator == 0) return to_string((int64_t)numerator / denominator);
        int64_t up = abs((int64_t)numerator), down = abs((int64_t)denominator);
        string ans;
        if ((numerator < 0) ^ (denominator < 0)) ans.push_back('-');
        ans += to_string(up / down) + '.';
        unordered_map<int64_t, int> re;
        int i = ans.size();
        up = up % down * 10;
        while (!re.count(up)) {
            if (up == 0) return ans;
            re[up] = i;
            ans.push_back('0' + up / down);
            i++;
            up = up % down * 10;
        }
        ans.insert(begin(ans) + re[up], '(');
        ans.push_back(')');
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.fractionToDecimal(1, 2) << endl;
    return 0;
}
