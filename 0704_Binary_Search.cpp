#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (nums[mid] == target) {
                return mid;
            }else if (nums[mid] < target) {
                l = mid;
            }else {
                r = mid - 1;
            }
        }
        return nums[l] == target ? l : -1;
    }
};

int main() {
    Solution s;
    vector<int> nums{-1, 0, 3, 5, 9, 12};
    int target = 9;
    cout << s.search(nums, target) << endl;
}

