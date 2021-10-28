#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_set>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool isPower(int n) {
        return (n & (n - 1)) == 0;
    }
    bool dfs(vector<int>& nums, int index, int curSum, vector<bool> &visited) {
        if (index == nums.size()) {
            return isPower(curSum);
        }
        int cur = -1;
        for (int i = 0; i < nums.size(); ++i) {
            if (!visited[i]) {
                cur = nums[i];
                if (index == 0 && cur == 0) continue;
                visited[i] = true;
                if (dfs(nums, index + 1, curSum * 10 + cur, visited))
                    return true;
                visited[i] = false;
            }
        }
        return false;
    }
    bool reorderedPowerOf2(int n) {
        vector<int> nums{};
        while (n > 0) {
            nums.push_back(n % 10);
            n /= 10;
        }
        // for (auto x : nums) cout << x << endl;
        vector<bool> visited(nums.size(), false);
        return dfs(nums, 0, 0, visited);
    }
};


class Solution2 {
public:
    unordered_set<string> re{};
    Solution2() {
        for (int i = 0; i < 30; ++i) {
            int n = 1 << i;
            re.insert(countDigits(n));
        }
    }

    string countDigits(int n) {
        string cnt(10, '0');
        while (n) {
            ++cnt[n % 10];
            n /= 10;
        }
        return cnt;
    }

    bool reorderedPowerOf2(int n) {
        return re.count(countDigits(n));
    }
};


int main() {
    Solution s;
    cout << s.reorderedPowerOf2(27486051) << endl;
    return 0;
}
