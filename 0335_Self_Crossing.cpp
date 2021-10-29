#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    bool isSelfCrossing(vector<int> &distance) {
        int n = distance.size();
        int i = 0;
        while (i < n && (i < 2 || distance[i] > distance[i - 2])) {
            ++i;
        }
        if (i == n) return false;

        if ((i == 3 && distance[i] == distance[i - 2]) || (i >= 4 && distance[i] >= distance[i - 2]  - distance[i - 4])) {
            distance[i - 1] -= distance[i - 3];
        }
        ++i;
        while (i < n && distance[i] < distance[i - 2]) {
            ++i;
        }
        return i != n;
    }
};

int main() {
    Solution s;
    vector<int> dis{1, 1, 2, 1, 1};
    cout << s.isSelfCrossing(dis) << endl;
    return 0;
}
