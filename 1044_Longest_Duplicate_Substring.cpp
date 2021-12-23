#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_set>
using namespace std;
typedef long long ll;

class Solution {
public:
    static constexpr int primer = 31;
    int check(vector<int> &arr, int len) {
        unsigned long long hash = 0;
        unsigned long long power = 1;

        for (int i = 0; i < len; ++i) {
            hash = hash * primer + arr[i];
            power *= primer;
        }

        unordered_set<unsigned long long> re{hash};
        for (int i = len; i < arr.size(); ++i) {
            hash = hash * primer - power * arr[i - len] + arr[i];
            if (re.count(hash)) return i - len + 1;
            re.insert(hash);
        }
        return -1;
    }
    string longestDupSubstring(string s) {
        int n = s.length();
        vector<int> arr;
        for (auto && ch : s) {
            arr.push_back(ch - 'a');
        }

        int l = 1, r = n - 1;
        int pos = -1, len = 0;
        while (l <= r) {
            int mid = l + (r - l + 1) / 2;
            int res = check(arr, mid);
            if (res == -1) {
                r = mid - 1;
            }else {
                l = mid + 1;
                len = mid;
                pos = res;
            }
        }

        return pos == -1 ? "" : s.substr(pos, len);
    }
};

int main() {
    Solution s;

    cout << s.longestDupSubstring("banana") << endl;
    cout << s.longestDupSubstring("abcd") << endl;
    cout << s.longestDupSubstring("aa") << endl;

    return 0;
}
