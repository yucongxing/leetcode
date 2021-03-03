#include <bits/stdc++.h>
using namespace std;
class Solution {
   public:
    int maxProduct(vector<int> &nums) {
        int ans = 1, maxans = nums[0];
        for (int i : nums) {
            ans *= i;
            if (ans >= maxans) maxans = ans;
            if (ans == 0) ans = 1;
        }
        return maxans;
    }
};
int main() {
    vector<int> nums{3, -1, 4};
    Solution s;
    printf("%d", s.maxProduct(nums));
    int a;
    scanf("%d", &a);
    printf("%d\n", a);
    for (auto n : nums) {
        cout << n << " ";
    }
    for (int i = 0; i < 12; i++) {
        printf("%d\n", a);
    }

    return 0;
}
