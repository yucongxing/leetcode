#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int x1 = max(ax1, bx1), y1 = max(ay1, by1), x2 = min(ax2, bx2), y2 = min(ay2, by2);
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - (x2 - x1) * (y2 - y1);
    }
};

int main() {
    Solution s;
    cout << s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) << endl;
    return 0;
}
