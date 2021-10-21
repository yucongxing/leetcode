#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        int carry{0}, n = digits.size();
        digits[n - 1]++;
        if (digits[n - 1] == 10) {
            digits[n - 1] = 0;
            carry = 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            if (carry == 0) break;
            digits[i] ++;
            if (digits[i] == 10) {
                digits[i] = 0;
                carry = 1;
            }else carry = 0;
        }
        if (carry == 1) digits.insert(digits.begin(), 1);
        return digits;
    }
};

int main() {
    Solution s;
    vector<int> digits{9, 9, 9};
    vector<int> ans = s.plusOne(digits);
    for (auto&& n : digits) {
        cout << n << endl;
    }
    return 0;
}
