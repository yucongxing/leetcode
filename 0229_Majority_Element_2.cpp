#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;


class Solution {
public:
    vector<int> majorityElement(vector<int> &nums) {
        int *a = nullptr, *b = nullptr;
        int ca = 0, cb = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (ca == 0 && cb == 0) {
                a = &nums[i];
                ++ca;
            }else if(ca == 0) {
                if (*b == nums[i]) {
                    ++cb;
                }else {
                    a = &nums[i];
                    ++ca;
                }
            }else if(cb == 0) {
                if (*a == nums[i]) {
                    ++ca;
                }else {
                    b = &nums[i];
                    ++cb;
                }
            }else {
                if (*a != nums[i] && *b != nums[i]) {
                    --ca;
                    --cb;
                }else if (*a == nums[i]) {
                    ++ca;
                }else {
                    ++cb;
                }
                if (ca == 0) {
                    a = nullptr;
                }
                if (cb == 0) {
                    b = nullptr;
                }
            }
        }
        vector<int> ans{};
        if (ca == cb && cb == 0) return ans;
        int cnt1 = 0, cnt2 = 0;
        for (int i = 0; i < n; ++i) {
            if (ca > 0 && *a == nums[i]) {
                ++cnt1;
            }
            if (cb > 0 && *b == nums[i]) {
                ++cnt2;
            }
        }
        if (cnt1 > n / 3) ans.push_back(*a);
        if (cnt2 > n / 3) ans.push_back(*b);
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> nums{2, 3, 2, 3};
    vector<int> ans = s.majorityElement(nums);
    for (auto n : ans) cout << n << endl;
    return 0;
}
