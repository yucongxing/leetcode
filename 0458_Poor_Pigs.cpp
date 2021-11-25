#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
typedef long long ll;

class Solution {
public:
    int poorPigs(int bukets, int minutesToDie, int minutesToTest) {
        int ans{0};
        while (pow(minutesToTest / minutesToDie + 1, ans) < bukets) {
            ++ans;
        }
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.poorPigs(1000, 15, 60) << endl;
    return 0;
}
