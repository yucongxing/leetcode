#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
typedef long long ll;

class Solution {
public:
    static constexpr double pi = M_PI;
    int visiblePoints(vector<vector<int>> &points, int angle, vector<int> &location) {
        int ans = 0;
        vector<double> angles;
        for (auto &&p : points) {
            int y = p[1] - location[1];
            int x = p[0] - location[0];

            if (x == 0 && y == 0) {
                ++ans;
                continue;
            }else if (x == 0 && y > 0) angles.push_back(pi / 2);
            else if (x == 0 && y < 0) angles.push_back(pi * 1.5);
            else {
                double t = double(y) / double(x);
                t = atan(t);
                if (x > 0 && y >= 0) angles.push_back(t);
                else if (x < 0 && y >= 0) angles.push_back(t + pi);
                else if (x < 0 && y <= 0) angles.push_back(t + pi);
                else if (x > 0 && y <= 0) angles.push_back(t + pi * 2);
            }
        }
        sort(angles.begin(), angles.end(), less<double>());
        int n = angles.size();
        int maxans = 0;
        for (int i = 0; i < n; ++i) {
            int tans = 0;
            double e = angles[i] + double(angle) / 180.0 * pi;
            auto start = angles.begin() + i;
            auto end = angles.end();
            if (e > pi * 2) {
                tans += n - i;
                e -= pi * 2;
                end = start;
                start = angles.begin();
            }
            auto it = upper_bound(start, end, e);
            tans += (it - start);
            maxans = max(tans, maxans);
        }
        return ans + maxans;
    }
};

int main() {
    Solution s;
    return 0;
}
