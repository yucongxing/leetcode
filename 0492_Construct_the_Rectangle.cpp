#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;
typedef long long ll;

class Solution {
public:
    vector<int> constructRectangle(int area) {
        int sq = sqrt(1.0 * area);
        vector<int> ans{};
        while (area % sq != 0) {
            --sq;
        }
        ans.push_back(area / sq);
        ans.push_back(sq);
        return ans;
    }
};

int main() {
    Solution s;
    int area = 2;
    vector<int> ans = s.constructRectangle(area);
    for (auto&& a : ans) cout << a << endl;
    return 0;
}
