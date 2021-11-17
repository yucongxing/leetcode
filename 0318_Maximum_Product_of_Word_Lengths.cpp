#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
using namespace std;
typedef long long ll;

class Solution {
public:
    int maxProduct(vector<string> &words) {
        unordered_map<int, int> m;
        for (auto &&w : words) {
            int mask{0};
            for (auto &&ch : w) {
                mask |= (1 << (ch - 'a'));
            }
            if (w.length() > m[mask]) {
                m[mask] = w.length();
            }
        }
        int res{0};
        for (auto &&p1 : m) {
            for (auto &&p2 : m) {
                if ((p1.first & p2.first) == 0) {
                    res = max(res, p1.second * p2.second);
                }
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    return 0;
}
