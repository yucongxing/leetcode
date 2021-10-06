#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int thirdMax(vector<int> &nums) {
        int *a = nullptr, *b = nullptr, *c = nullptr;
        for (auto &num : nums) {
            if (a == nullptr || num > *a) {
                c = b;
                b = a;
                a = &num;
            }else if (num < *a && (b == nullptr || num > *b)) {
                c = b;
                b = &num;
            }else if (b != nullptr && *b > num && (c != nullptr || num > *c)) {
                c = &num;
            }
        }
        return c == nullptr ? *a : *c;
    }
};

int main() {
    Solution s;
    vector<int> nums{3, 2, 1};
    cout << s.thirdMax(nums) << endl;
    return 0;
}
