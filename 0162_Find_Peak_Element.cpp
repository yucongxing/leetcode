#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + ((r - l) >> 1);
            if (mid < n - 1 && nums[mid] < nums[mid + 1]) {
                l = mid + 1;
            }else {
                r = mid;
            }
            //cout << l << endl;
        }
        return l;
    }
};

int main() {
    Solution s;
    vector<int> nums{1,2,3,1};
    cout << s.findPeakElement(nums) << endl;
}
