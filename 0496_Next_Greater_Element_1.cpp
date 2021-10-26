#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <unordered_map>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int> &nums2) {
        stack<int> s{};
        unordered_map<int, int> re{};
        s.push(nums2[0]);
        for (int i = 1; i < nums2.size(); ++i) {
            if(nums2[i] < s.top()) {
                s.push(nums2[i]);
            }else {
                while (!s.empty() && nums2[i] > s.top()) {
                    re[s.top()] = nums2[i];
                    s.pop();
                }
                s.push(nums2[i]);
            }
        }
        vector<int> ans(nums1.size(), -1);
        for (int i = 0; i < nums1.size(); ++i) {
            if (re.count(nums1[i])) {
                ans[i] = re[nums1[i]];
            }
        }
        return ans;
    }
};
//单调栈 + hashmap

int main() {
    Solution s;
    vector<int> nums1{4, 1, 2};
    vector<int> nums2{1, 3, 4, 2};
    vector<int> ans = s.nextGreaterElement(nums1, nums2);
    for (auto && a : ans) cout << a << endl;;
    return 0;
}
