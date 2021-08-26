#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int n = people.size();
        int ans = 0;
        int used = 0;
        for (int i = n-1; i > used; i--) {
            if (limit - people[i] >= people[used]) {
                used++;
                ans++;
            }else {
                ans++;
            }
            if (used == i - 1) {
                ans ++;
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> people = {3, 5, 3, 4};
    int limit = 5;
    cout << s.numRescueBoats(people, limit) << endl;
}
