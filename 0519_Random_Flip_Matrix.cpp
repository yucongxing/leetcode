#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
typedef long long ll;

class Solution {
public:
    int m{0}, n{0}, total{0};
    unordered_map<int, int> re{};
    Solution() = default;
    Solution(int _m, int _n) : m(_m), n(_n), total(_m * _n) {}

    vector<int> flip() {
        int x = rand() % total;
        total--;
        auto ret = re.find(x);
        if (ret != re.end()) {
            x = re[x];
        }

        ret = re.find(total);
        if (ret != re.end()) {
            re[x] = re[total];
        }else {
            re[x] = total;
        }
        return {x / n, x % n};
    }

    void reset() {
        total = m * n;
        re.clear();
    }
};

int main() {
    Solution s;
    return 0;
}
