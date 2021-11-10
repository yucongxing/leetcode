#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int findPoisonedDuration(vector<int> &timeSeries, int duration) {
        int ans{0};
        for (int i = 1; i < timeSeries.size(); ++i) {
            if (timeSeries[i] - timeSeries[i - 1] < duration) {
                ans += timeSeries[i] - timeSeries[i - 1];
            }else {
                ans += 2 ;
            }
        }
        ans += 2;
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> timeSeries{1, 4};
    cout << s.findPoisonedDuration(timeSeries, 2) << endl;
    return 0;
}
