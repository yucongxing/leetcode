#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums){
        int i = nums.size() - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
                i--;
        }
        if (i >= 0) {
            int j = nums.size() - 1;
            while (j >= 0 && nums[i] >= nums[j]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};

int main(){
    Solution s;
    vector<int> v = {1, 2, 3};
    s.nextPermutation(v);
    for (auto x : v) {
        cout<< x << " " <<endl;
    }
    return 0;
}

